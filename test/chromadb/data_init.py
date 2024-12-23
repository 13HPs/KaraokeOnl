import chromadb
from chromadb.utils import embedding_functions
from pymongo import MongoClient
from utils import *
import time
start_time = time.time()
# Connection string
connection_string = "mongodb+srv://leminh:d9wcwbu0QAfyCcLv@karaoke.bjdua.mongodb.net/karaoke?retryWrites=true&w=majority&appName=karaoke"
# Replace <password> with your actual password
client = MongoClient(connection_string)

# Database and collection
db = client.karaoke  # Connect to the database
musics_collection = db.musics  # Collection with music data
accounts_collection = db.accounts #Collection with artist data

# Query to retrieve the list of lyrics
lyrics_list = []
for music in musics_collection.find():
    music_id = str(music["_id"])
    for lyric in music.get("lyrics", []):
        lyrics_list.append({
            "music_id": music_id,
            "text": lyric["text"],
            "order": lyric["order"]
        })
query = {"_cls": "Account.ExtendedAccount.Artist"}
artists_results = accounts_collection.find(query)
artists_list = []
for artist in artists_results:
    artist_id = str(artist["_id"])
    artists_list.append({
        "artist_id": artist_id,
        "name": artist["name"]
    })
musics_list = []
for music in musics_collection.find():
    music_id = str(music["_id"])
    music_name = music["name"]
    musics_list.append({
        "music_id": music_id,
        "name": music_name
    })
end_time = time.time()
print(f"MongoDB: {end_time - start_time} seconds")
default_emb = embedding_functions.DefaultEmbeddingFunction()
vie_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="dangvantuan/vietnamese-embedding",
    device="cuda")
query_cosine = {"hnsw:space": "cosine"}
query_l2 = {"hnsw:space": "l2"}
query_ip = {"hnsw:space": "ip"}
start_time = time.time()
chroma_client = chromadb.PersistentClient(path="D:\PBL6\chromadb_database")
# musics_collection = chroma_client.create_collection("musics_collection",
#                                                     embedding_function=default_emb,
#                                                     metadata=query_l2)
# artists_collection = chroma_client.create_collection("artists_collection",
#                                                      embedding_function=default_emb,
#                                                      metadata=query_l2)
lyrics_collection = chroma_client.create_collection("lyrics_collection",
                                                    embedding_function=vie_ef,
                                                    metadata=query_cosine)
# musics_collection = chroma_client.get_collection("musics_collection")
# artists_collection = chroma_client.get_collection("artists_collection")
# lyrics_collection = chroma_client.get_collection("lyrics_collection")
# musics_collection.upsert(
#     ids=[music["music_id"] for music in musics_list],
#     documents=[music["name"] for music in musics_list]
# )
# artists_collection.upsert(
#     ids=[artist["artist_id"] for artist in artists_list],
#     documents=[artist["name"] for artist in artists_list]
# )

chunked_lyrics_list = []
def split_lyrics(lyrics_list, chunk_size=100):
    chunks = []
    start = 0
    while start < len(lyrics_list):
        end = start + chunk_size
        chunks.append(lyrics_list[start:end])
        start = end
    return chunks

lyrics_chunks = split_lyrics(lyrics_list)
total_records = lyrics_collection.count()
print(f"Before insert lyrics to ChromaDB:{total_records}")
count = 0
skipcount = 0
duplicate_count = 0
id_set = set()
skipped_ids = set()
for chunk in lyrics_chunks:
    for lyric in chunk:
        text = lyric["text"]
        order = lyric["order"]
        music_id = lyric["music_id"]
        ids = f"lyric_{order}_{music_id}"
        print(f"Insert id: {ids}")
        if ids not in id_set:
            lyrics_collection.upsert(
                ids=ids,
                documents=[text],
                metadatas=[{
                    "music_id": music_id
                }]
            )
            id_set.add(ids)
        else:
            print("========================================================")
            print(f"Duplicate id: {ids}")
            print("========================================================")
            skipcount += 1
            skipped_ids.add(music_id)
        count += 1
    print(f"{count} lyrics inserted")
print(f"number of lyrics:{count}")
print(f"Processed IDs: {len(id_set)}")
print(f"Skipped IDs: {len(skipped_ids)}, skip count: {skipcount}, duplicate count: {duplicate_count}")
end_time = time.time()
print(f"Chroma create and insert: {end_time - start_time} seconds")
total_records = lyrics_collection.count()
print(f"After insert lyrics to ChromaDB:{total_records}")
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
# query = "Nhìn đâu thì em cũng duyệt"
# results = query_all_collections_with_comparison(query,
#                                                 artists_collection,
#                                                 musics_collection,
#                                                 lyrics_collection
#                                                 )
#
# print(results)