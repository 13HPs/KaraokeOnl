from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from whoosh import scoring
import os
import base64

# Step 1: Define schema
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), path=ID(stored=True))

# Step 2: Create index
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = create_in("indexdir", schema)

# Step 3: Add encoded content
writer = ix.writer()

# Vietnamese text to index
from pyvi import ViTokenizer
import unicodedata
import base64

vietnamese_stopwords = {"là", "và", "có"}

def preprocess_vietnamese_text(text, remove_diacritics_flag=False, encode=False):
    # Normalize text
    text = unicodedata.normalize('NFC', text)
    # Lowercase text
    text = text.lower()
    # Remove diacritics (optional)
    if remove_diacritics_flag:
        text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    # Tokenize text
    text = ViTokenizer.tokenize(text)
    # Remove stopwords
    words = text.split()
    text = ' '.join(word for word in words if word not in vietnamese_stopwords)
    # Encode text (optional)
    if encode:
        text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return text

# Example usage
text = "Tiếng Việt là ngôn ngữ rất đặc biệt."
text1 = "Tiếng Anh là ngôn ngữ như l."
processed_text = preprocess_vietnamese_text(text, remove_diacritics_flag=True, encode=False)
processed_text1 = preprocess_vietnamese_text(text1, remove_diacritics_flag=True, encode=False)
# encoded_text = base64.b64encode(processed_text.encode('utf-8')).decode('utf-8')

writer.add_document(title="Example Document", content=processed_text, path="/example")
writer.add_document(title="Example Document2", content=processed_text1, path="/example")
writer.commit()
# Step 4: Query and decode
with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
    docnum = 0  # Document number to compare (e.g., first document in index)
    query = QueryParser("content", ix.schema).parse(preprocess_vietnamese_text("Tiếng Anh",remove_diacritics_flag=True, encode=False))
    results = searcher.more_like(docnum, "content", top=5)
    # results = searcher.search(query)
    print(results)
    for result in results:
        # decoded_content = base64.b64decode(result['content'].encode('utf-8')).decode('utf-8')
        print(f"Title: {result['title']}")
        print(f"Score: {result.score}")
        # print(f"Decoded Content: {decoded_content}")
