import chromadb

from chromadb.utils import embedding_functions

default_emb = embedding_functions.DefaultEmbeddingFunction()
chroma_client = chromadb.PersistentClient(path="./test/chromadb/chromadb_db")

# music_collection = chroma_client.create_collection("music_collection", embedding_function=default_emb)
# artist_collection = chroma_client.create_collection("artist_collection", embedding_function=default_emb)
music_collection = chroma_client.get_collection("music_collection")
artist_collection = chroma_client.get_collection("artist_collection")


# Create the `artists` collection
artists = [
    {"id": "artist1", "name": "Son Tung MTP"},
    {"id": "artist2", "name": "Jack 97"},
    {"id": "artist3", "name": "Dalab"},
    {"id": "artist4", "name": "Maroon5"},
    {"id": "artist5", "name": "One Direction"},
    {"id": "artist6", "name": "Taylor Swift"},
    {"id": "artist7", "name": "The Weeknd"}
]
artist_collection.upsert(
    ids=[artist["id"] for artist in artists],
    documents=[artist["name"] for artist in artists]
)

# Create the `music` collection
music = [
    {"id": "music1", "artist_id": ["artist1", "artist2"], "name": "Chung ta khong thuoc ve nhau", "genre": "pop"},
    {"id": "music2", "artist_id": "artist1", "name": "Dung lam trai tim anh dau"},
    {"id": "music3", "artist_id": "artist1", "name": "Am tham ben em"},
    {"id": "music4", "artist_id": "artist2", "name": "Thien Ly oi"},
    {"id": "music5", "artist_id": "artist2", "name": "Hong nhan bac phan"},
    {"id": "music6", "artist_id": "artist3", "name": "Bau troi moi"},
    {"id": "music7", "artist_id": "artist3", "name": "Chay khoi the gioi nay"},
    {"id": "music8", "artist_id": "artist4", "name": "Stereo heart"},
    {"id": "music9", "artist_id": "artist4", "name": "Sugar"},
    {"id": "music10", "artist_id": "artist5", "name": "Diana"},
    {"id": "music11", "artist_id": "artist5", "name": "Hip Hop Track"},
    {"id": "music12", "artist_id": "artist6", "name": "Blank space"},
    {"id": "music13", "artist_id": "artist6", "name": "Cruel Summer"},
    {"id": "music14", "artist_id": "artist7", "name": "Blidding light"},
    {"id": "music15", "artist_id": "artist7", "name": "Save your tears"},
]
lyric = [
    {"id": "lyrics1",
     "music_id": "music1",
     "order": 1,
     "text": "Về về về nơi này",
     "start_time": "00:00:04.780", "end_time": "00:00:08.240", "artist_index": 0},
    {"id": "lyrics2",
     "music_id": "music1",
     "order": 2,
     "text": "Chúng ta không thuộc về nhau",
     "start_time": "00:00:08.240", "end_time": "00:00:12.300", "artist_index": 0},
    {"id": "lyrics3",
     "music_id": "music1",
     "order": 3,
     "text": "Chúng ta không thuộc về",
     "start_time": "00:00:12.980", "end_time": "00:00:14.560", "artist_index": 0},
    {"id": "lyrics4",
     "music_id": "music1",
     "order": 4,
     "text": "Về về về nơi này",
     "start_time": "00:00:14.560", "end_time": "00:00:17.760", "artist_index": 0},
    {"id": "lyrics5",
     "music_id": "music1",
     "order": 5,
     "text": "Niềm tin đã mất,",
     "start_time": "00:00:17.760", "end_time": "00:00:19.340", "artist_index": 0},
    {"id": "lyrics6",
     "music_id": "music1",
     "order": 6,
     "text": "Giọt nước mắt cuốn ký ức anh chìm sâu",
     "start_time": "00:00:19.340", "end_time": "00:00:22.270", "artist_index": 0},
    {"id": "lyrics7",
     "music_id": "music1",
     "order": 7,
     "text": "Tình về nơi đâu,",
     "start_time": "00:00:22.270", "end_time": "00:00:23.870", "artist_index": 0},
]
music_collection.upsert(
    ids=[music_item["id"] for music_item in music],
    documents=[music_item["name"] for music_item in music],
    metadatas=[{"artist_id": music_item["artist_id"]} for music_item in music]
)

# Query the artist_collection for similar artist names
query = "SonTung"
results = artist_collection.query(
    query_texts=[query],
    n_results=15  # Number of similar results to return
)
print(results)

# Extract artist IDs from the results
artist_ids = results["ids"][0]
print(artist_ids)
# Query the music collection for songs by the artist IDs
music_results = music_collection.query(
    where={"artist_id": {"$in": artist_ids}},  # Use artist IDs to filter
    n_results=50,  # Adjust this limit as needed
    query_texts=[""]  # Add a placeholder to satisfy the requirement
)

# Extract music details
music_list = [
    {
        "music_id": result_id,
        "music_name": result_doc,
        "artist_id": result_meta["artist_id"]
    }
    for result_id, result_doc, result_meta in zip(
        music_results["ids"][0],  # Music IDs
        music_results["documents"][0],  # Music names
        music_results["metadatas"][0]  # Metadata (artist_id)
    )
]


final_results = []
# Iterate over the results by index to match IDs and documents
for idx, artist_name in enumerate(results["documents"][0]):  # Artist names
    artist_id = results["ids"][0][idx]  # Corresponding artist ID
    # Find music associated with this artist ID
    artist_music = [
        music
        for music in music_list
        if music["artist_id"] == artist_id
    ]
    final_results.append({
        "artist_name": artist_name,
        "music": artist_music
    })

# Display final results
for result in final_results:
    print(f"Artist: {result['artist_name']}")
    print("Music:")
    for song in result["music"]:
        print(f" - {song['music_name']}")

# Output final results
for result in final_results:
    print(f"Artist: {result['artist_name']}")
    print("Music:")
    for song in result["music"]:
        print(f" - {song['music_name']}")


