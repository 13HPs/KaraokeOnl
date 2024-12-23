import time

lyric = [
    {
        "music_id": "music1",
        "order": 1,
        "text": "Về về về nơi này"
    },
    {
        "music_id": "music1",
        "order": 2,
        "text": "Chúng ta không thuộc về nhau"
    },
    {
        "music_id": "music1",
        "order": 3,
        "text": "Chúng ta không thuộc về"
    },
    {
        "music_id": "music1",
        "order": 4,
        "text": "Về về về nơi này"
    },
    {
        "music_id": "music1",
        "order": 5,
        "text": "Niềm tin đã mất,"
    },
    {
        "music_id": "music1",
        "order": 6,
        "text": "Giọt nước mắt cuốn ký ức anh chìm sâu"
    },
    {
        "music_id": "music1",
        "order": 7,
        "text": "Tình về nơi đâu,"
    },
    {
        "music_id": "music17",
        "order": 1,
        "text": "Lost in the echo of time"
    },
    {
        "music_id": "music17",
        "order": 2,
        "text": "Every star fades away"
    },
    {
        "music_id": "music17",
        "order": 3,
        "text": "The rhythm of the heart"
    },
    {
        "music_id": "music17",
        "order": 4,
        "text": "Lights guide me home"
    },
    {
        "music_id": "music17",
        "order": 5,
        "text": "Dancing shadows on the wall"
    },
    {
        "music_id": "music17",
        "order": 6,
        "text": "Endless whispers in the night"
    },
    {
        "music_id": "music17",
        "order": 7,
        "text": "Where dreams collide"
    },
    {
        "music_id": "music18",
        "order": 1,
        "text": "Counting stars in the dark"
    },
    {
        "music_id": "music18",
        "order": 2,
        "text": "Chasing shadows through the haze"
    },
    {
        "music_id": "music18",
        "order": 3,
        "text": "Every heartbeat, a melody"
    },
    {
        "music_id": "music18",
        "order": 4,
        "text": "Silent echoes fill the air"
    },
    {
        "music_id": "music18",
        "order": 5,
        "text": "A symphony of forgotten songs"
    },
    {
        "music_id": "music18",
        "order": 6,
        "text": "The rhythm flows through my soul"
    },
    {
        "music_id": "music18",
        "order": 7,
        "text": "Where memories never fade"
    },
    {
        "music_id": "music19",
        "order": 1,
        "text": "Memories linger in the rain"
    },
    {
        "music_id": "music19",
        "order": 2,
        "text": "A spark ignites the fire within"
    },
    {
        "music_id": "music19",
        "order": 3,
        "text": "Every note tells a story"
    },
    {
        "music_id": "music19",
        "order": 4,
        "text": "The harmony of our souls"
    },
    {
        "music_id": "music19",
        "order": 5,
        "text": "In every whisper, a song"
    },
    {
        "music_id": "music19",
        "order": 6,
        "text": "The rhythm of eternity"
    },
    {
        "music_id": "music19",
        "order": 7,
        "text": "Forever in your embrace"
    },
    {
        "music_id": "music20",
        "order": 8,
        "text": "Lost in the melody"
    },
    {
        "music_id": "music21",
        "order": 9,
        "text": "Whispers in the night"
    },
    {
        "music_id": "music22",
        "order": 10,
        "text": "Echoes of memories"
    },
    {
        "music_id": "music23",
        "order": 11,
        "text": "Fading into the distance"
    },
    {
        "music_id": "music24",
        "order": 12,
        "text": "Shadows on the wall"
    },
    {
        "music_id": "music25",
        "order": 32,
        "text": "Tình yêu mãi mãi không phai"
    },
    {
        "music_id": "music26",
        "order": 19,
        "text": "Mưa đêm qua phố"
    },
    {
        "music_id": "music27",
        "order": 41,
        "text": "Em ơi, anh vẫn nhớ"
    },
    {
        "music_id": "music28",
        "order": 11,
        "text": "Tâm hồn của tôi"
    },
    {
        "music_id": "music29",
        "order": 28,
        "text": "Đừng xa em đêm nay"
    },
    {
        "music_id": "music30",
        "order": 35,
        "text": "Nhạc tình yêu"
    },
    {
        "music_id": "music31",
        "order": 22,
        "text": "Gió mùa thu"
    },
    {
        "music_id": "music32",
        "order": 49,
        "text": "Tình yêu và nỗi nhớ"
    },
    {
        "music_id": "music33",
        "order": 15,
        "text": "Em ơi, anh vẫn yêu"
    },
    {
        "music_id": "music34",
        "order": 38,
        "text": "Đêm nay anh cô đơn"
    },
    {
        "music_id": "music35",
        "order": 25,
        "text": "Tình yêu không có lỗi"
    },
    {
        "music_id": "music36",
        "order": 42,
        "text": "Mưa bay về nơi đâu"
    },
    {
        "music_id": "music37",
        "order": 18,
        "text": "Anh vẫn nhớ em"
    },
    {
        "music_id": "music38",
        "order": 31,
        "text": "Tâm hồn của em"
    },
    {
        "music_id": "music39",
        "order": 46,
        "text": "Đừng bỏ em"
    },
    {
        "music_id": "music40",
        "order": 13,
        "text": "Tình yêu không chết"
    },
    {
        "music_id": "music41",
        "order": 29,
        "text": "Gió mùa xuân"
    },
    {
        "music_id": "music42",
        "order": 44,
        "text": "Em ơi, anh vẫn yêu"
    },
    {
        "music_id": "music43",
        "order": 20,
        "text": "Tình yêu và nỗi nhớ"
    },
    {
        "music_id": "music44",
        "order": 36,
        "text": "Đêm nay anh cô đơn"
    },
    {
        "music_id": "music45",
        "order": 48,
        "text": "Tình yêu không có lỗi"
    },
    {
        "music_id": "music46",
        "order": 14,
        "text": "Mưa bay về nơi đâu"
    },
    {
        "music_id": "music47",
        "order": 40,
        "text": "Anh vẫn nhớ em"
    },
    {
        "music_id": "music48",
        "order": 23,
        "text": "Tâm hồn của em"
    },
    {
        "music_id": "music49",
        "order": 34,
        "text": "Đừng bỏ em"
    },
    {
        "music_id": "music50",
        "order": 17,
        "text": "Tình yêu không chết"
    },
    {
        "music_id": "music51",
        "order": 30,
        "text": "Gió mùa thu"
    },
    {
        "music_id": "music52",
        "order": 45,
        "text": "Em ơi, anh vẫn yêu"
    },
    {
        "music_id": "music53",
        "order": 21,
        "text": "Tình yêu và nỗi nhớ"
    },
    {
        "music_id": "music54",
        "order": 39,
        "text": "Đêm nay anh cô đơn"
    },
    {
        "music_id": "music55",
        "order": 16,
        "text": "Tình yêu không có lỗi"
    },
    {
        "music_id": "music56",
        "order": 43,
        "text": "Mưa bay về nơi đâu"
    },
    {
        "music_id": "music57",
        "order": 24,
        "text": "Anh vẫn nhớ em"
    },
    {
        "music_id": "music58",
        "order": 33,
        "text": "Tâm hồn"
    }
]

music = [
    {"id": "music1", "name": "Am tham ben em"},
    {"id": "music16", "name": "Chung ta khong thuoc ve nhau"},
    {"id": "music2", "name": "Dung lam trai tim anh dau"},
    {"id": "music3", "name": "Am tham ben em"},
    {"id": "music4", "name": "Thien Ly oi"},
    {"id": "music5", "name": "Hong nhan bac phan"},
    {"id": "music6", "name": "Bau troi moi"},
    {"id": "music7", "name": "Chay khoi the gioi nay"},
    {"id": "music8", "name": "Stereo heart"},
    {"id": "music9", "name": "Sugar"},
    {"id": "music10", "name": "Diana"},
    {"id": "music11", "name": "Hip Hop Track"},
    {"id": "music12", "name": "Blank space"},
    {"id": "music13", "name": "Cruel Summer"},
    {"id": "music14", "name": "Blidding light"},
    {"id": "music15", "name": "Save your tears"},
    {"id": "music17", "name": "Lost Stars"},
    {"id": "music18", "name": "Counting Stars"},
    {"id": "music19", "name": "Memories"},
    {"id": "music20", "name": "All of Me"},
    {"id": "music21", "name": "Someone Like You"},
    {"id": "music22", "name": "Hello"},
    {"id": "music23", "name": "Rolling in the Deep"},
    {"id": "music24", "name": "Skyfall"},
    {"id": "music25", "name": "Let Her Go"},
    {"id": "music26", "name": "Photograph"},
    {"id": "music27", "name": "Thinking Out Loud"},
    {"id": "music28", "name": "Perfect"},
    {"id": "music29", "name": "Shape of You"},
    {"id": "music30", "name": "Bad Habits"},
    {"id": "music31", "name": "Happier"},
    {"id": "music32", "name": "Shivers"},
    {"id": "music33", "name": "Believer"},
    {"id": "music34", "name": "Thunder"},
    {"id": "music35", "name": "Demons"},
    {"id": "music36", "name": "Radioactive"},
    {"id": "music37", "name": "On Top of the World"},
    {"id": "music38", "name": "It's Time"},
    {"id": "music39", "name": "Bleeding Love"},
    {"id": "music40", "name": "Levitating"},
    {"id": "music41", "name": "Don't Start Now"},
    {"id": "music42", "name": "One Kiss"},
    {"id": "music43", "name": "New Rules"},
    {"id": "music44", "name": "Break My Heart"},
    {"id": "music45", "name": "Physical"},
    {"id": "music46", "name": "Electricity"},
    {"id": "music47", "name": "Cold Heart"},
    {"id": "music48", "name": "Stay"},
    {"id": "music49", "name": "Sunflower"},
    {"id": "music50", "name": "Circles"},
    {"id": "music51", "name": "Wow"},
    {"id": "music52", "name": "Congratulations"},
    {"id": "music53", "name": "Better Now"},
    {"id": "music54", "name": "Rockstar"},
    {"id": "music55", "name": "Go Flex"},
    {"id": "music56", "name": "White Iverson"},
    {"id": "music57", "name": "Hollywood's Bleeding"},
    {"id": "music58", "name": "Goodbyes"},
    {"id": "music59", "name": "Psycho"},
    {"id": "music60", "name": "Wow Remix"},
    {"id": "music61", "name": "Circles Acoustic"},
    {"id": "music62", "name": "Deja Vu"},
    {"id": "music63", "name": "Happier Than Ever"},
    {"id": "music64", "name": "Therefore I Am"},
    {"id": "music65", "name": "Ocean Eyes"},
    {"id": "music66", "name": "Everything I Wanted"},
    {"id": "music67", "name": "My Future"},
    {"id": "music68", "name": "Your Power"},
    {"id": "music69", "name": "Bellyache"},
    {"id": "music70", "name": "When The Party's Over"},
    {"id": "music71", "name": "Lovely"},
    {"id": "music72", "name": "Six Feet Under"},
    {"id": "music73", "name": "Bored"},
    {"id": "music74", "name": "I Love You"},
    {"id": "music75", "name": "Listen Before I Go"},
    {"id": "music76", "name": "8"},
    {"id": "music77", "name": "Xanny"},
    {"id": "music78", "name": "All The Good Girls Go To Hell"},
    {"id": "music79", "name": "You Should See Me in a Crown"},
    {"id": "music80", "name": "Wish You Were Gay"},
    {"id": "music81", "name": "Bury a Friend"},
    {"id": "music82", "name": "Ilomilo"},
    {"id": "music83", "name": "No Time To Die"},
    {"id": "music84", "name": "Lost Cause"},
    {"id": "music85", "name": "Everything We Know"},
    {"id": "music86", "name": "Copycat"},
    {"id": "music87", "name": "The End of the World"},
    {"id": "music88", "name": "No Such Thing as a Broken Heart"},
    {"id": "music89", "name": "Meant to Be"},
    {"id": "music90", "name": "Tequila"},
    {"id": "music91", "name": "10,000 Hours"},
    {"id": "music92", "name": "Speechless"},
    {"id": "music93", "name": "Die From a Broken Heart"},
    {"id": "music94", "name": "I Hope"},
    {"id": "music95", "name": "One Man Band"},
    {"id": "music96", "name": "Homesick"},
    {"id": "music97", "name": "Take Me Home"},
    {"id": "music98", "name": "Love Wins"},
    {"id": "music99", "name": "Boy"},
    {"id": "music100", "name": "Slow Down"},
]

artists = [
    {"id": "artist1", "name": "Son Tung MTP"},
    {"id": "artist2", "name": "Jack"},
    {"id": "artist3", "name": "Dalab"},
    {"id": "artist4", "name": "Maroon5"},
    {"id": "artist5", "name": "One Direction"},
    {"id": "artist6", "name": "Taylor Swift"},
    {"id": "artist7", "name": "The Weeknd"},
    {"id": "artist8", "name": "Huu hiep"},
    {"id": "artist9", "name": "Ed Sheeran"},
    {"id": "artist10", "name": "Adele"},
    {"id": "artist11", "name": "Justin Bieber"},
    {"id": "artist12", "name": "BTS"},
    {"id": "artist13", "name": "Coldplay"},
    {"id": "artist14", "name": "Shawn Mendes"},
    {"id": "artist15", "name": "Katy Perry"},
    {"id": "artist16", "name": "Bruno Mars"},
    {"id": "artist17", "name": "Post Malone"},
    {"id": "artist18", "name": "Dua Lipa"},
    {"id": "artist19", "name": "Billie Eilish"},
    {"id": "artist20", "name": "Harry Styles"},
    {"id": "artist21", "name": "Olivia Rodrigo"},
    {"id": "artist22", "name": "Lil Nas X"},
    {"id": "artist23", "name": "Doja Cat"},
    {"id": "artist24", "name": "Imagine Dragons"},
    {"id": "artist25", "name": "Ariana Grande"},
    {"id": "artist26", "name": "Sia"},
    {"id": "artist27", "name": "Halsey"},
    {"id": "artist28", "name": "The Chainsmokers"},
    {"id": "artist29", "name": "Zayn Malik"},
    {"id": "artist30", "name": "Camila Cabello"},
    {"id": "artist31", "name": "Charlie Puth"},
    {"id": "artist32", "name": "Sam Smith"},
    {"id": "artist33", "name": "Selena Gomez"},
    {"id": "artist34", "name": "John Legend"},
    {"id": "artist35", "name": "Lana Del Rey"},
    {"id": "artist36", "name": "Rihanna"},
    {"id": "artist37", "name": "Drake"},
    {"id": "artist38", "name": "J Balvin"},
    {"id": "artist39", "name": "Bad Bunny"},
    {"id": "artist40", "name": "Tones and I"},
    {"id": "artist41", "name": "Jason Derulo"},
    {"id": "artist42", "name": "Megan Thee Stallion"},
    {"id": "artist43", "name": "Lizzo"},
    {"id": "artist44", "name": "Khalid"},
    {"id": "artist45", "name": "Calvin Harris"},
    {"id": "artist46", "name": "Marshmello"},
    {"id": "artist47", "name": "Alan Walker"},
    {"id": "artist48", "name": "Kygo"},
    {"id": "artist49", "name": "Avicii"},
    {"id": "artist50", "name": "David Guetta"}
]

import chromadb
from chromadb.utils import embedding_functions

start_time = time.time()
chroma_client = chromadb.PersistentClient(path="./test/chromadb/chromadb_db")

#Embedding Function
default_emb = embedding_functions.DefaultEmbeddingFunction()
sentence_transformers_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="dangvantuan/vietnamese-embedding",
    device="cuda")

#Query algorithm
query_cosine = {"hnsw:space": "cosine"}
query_l2 = {"hnsw:space": "l2"}
query_ip = {"hnsw:space": "ip"}
musics_collection = chroma_client.create_collection("musics_collection",
                                                    embedding_function=default_emb,
                                                    metadata=query_l2)
artists_collection = chroma_client.create_collection("artists_collection",
                                                     embedding_function=default_emb,
                                                    metadata=query_l2)
lyrics_collection = chroma_client.create_collection("lyrics_collection",
                                                    embedding_function=default_emb,
                                                    metadata=query_l2)
# musics_collection = chroma_client.get_collection("musics_collection")
# artists_collection = chroma_client.get_collection("artists_collection")
# lyrics_collection = chroma_client.get_collection("lyrics_collection")

musics_collection.upsert(
    ids=[song["id"] for song in music],
    documents=[song["name"] for song in music]
)
artists_collection.upsert(
    ids=[artist["id"] for artist in artists],
    documents=[artist["name"] for artist in artists]
)
lyrics_collection.upsert(
    ids=[f"lyric_{i}" for i in range(len(lyric))],
    documents=[lyric["text"] for lyric in lyric],
    metadatas=[{
        "music_id": lyric["music_id"],
        "order": lyric["order"]
    } for lyric in lyric]
)
end_time = time.time()
print(f"Time taken to load data and insert: {end_time - start_time} seconds")

from utils import *
query = input("Enter your query: ")
n_results = int(input("Enter the number of results to display (default is 10): "))
start_time = time.time()
results = query_all_collections_with_comparison(query,
                                                artists_collection,
                                                musics_collection,
                                                lyrics_collection,
                                                n_results)
flag = results["most_relevant"]
print(f"Query: {query}")
if flag == "lyrics":
    final_results = extract_lyrics_details(results["results"])
    end_time = time.time()
    print("Query Time:", end_time - start_time)
    print("Most Relevant Collection:", flag)
    print("Lyric Details:")
    for detail in final_results:
        print(f"Lyric: {detail['lyric_content']} - "
              f"Music ID: {detail['music_id']} - "
              f"Order: {detail['lyric_order']} - "
              f"Distance: {detail['distance']}."
              f"")
    end_time = time.time()
    print("Full Time:", end_time - start_time)
elif flag == "artists":
    artists_results = extract_artists_details(results["results"])
    end_time = time.time()
    print("Query Time:", end_time - start_time)
    print("Most Relevant Collection:", flag)
    print("Artists Details:")
    for detail in artists_results:
        print(f"Name: {detail['name']} - "
              f"Artist ID: {detail['artist_id']} - "
              f"Distance: {detail['distance']}."
              f"")
    end_time = time.time()
    print("Full Time:", end_time - start_time)
elif flag == "musics":
    musics_results = extract_musics_details(results["results"])
    end_time = time.time()
    print("Query Time:", end_time - start_time)
    print("Most Relevant Collection:", flag)
    print("Music Details:")
    for detail in musics_results:
        print(f"Name: {detail['name']} - "
              f"Music ID: {detail['music_id']} - "
              f"Distance: {detail['distance']}."
              f"")
    end_time = time.time()
    print("Full Time:", end_time - start_time)