import os
import json
import chromadb
from chromadb.config import Settings
from openai_embedding_function import get_openai_ef

from pprint import pprint as pp
from dotenv import load_dotenv

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
PERSIST_DIRECTORY = os.getenv("PERSIST_DIRECTORY")
DATA_PATH_1 = "../scrape/mckinsey/data/content.json"
DATA_PATH_2 = "../scrape/accenture/data/content_complete.json"

def prepare_mckinsey_data(path):
    with open(path, 'r') as f:
        data = json.load(f)
    documents = [''.join(doc['paragraphs']) for doc in data]
    metadatas = [{'title': doc['title'], 'description': ''.join(doc['description']),
                  'link': doc['link']} for doc in data]
    ids = [str(i) for i in range(len(data))]
    print(len(documents), len(metadatas), len(ids))
    return documents, metadatas, ids

def prepare_accenture_data(path, ids):
    max_id = max([int(i) for i in ids]) # avoid overwriting ids from mckinsey
    with open(path, 'r') as f:
        data = json.load(f)
    documents = [doc['text'] for doc in data] #we already did join in scrape. my bad
    metadatas = [{'title': doc['title'], 'description': ''.join(doc['description']),
                  'link': doc['link']} for doc in data]
    ids = [str(i+max_id) for i in range(len(data))]
    print(len(documents), len(metadatas), len(ids))
    return documents, metadatas, ids


if __name__ == "__main__":

    chroma_client = chromadb.Client(
        Settings(persist_directory=PERSIST_DIRECTORY, chroma_db_impl="duckdb+parquet"))
    try: 
        chroma_client.delete_collection(name=COLLECTION_NAME)
    except:
        collection = chroma_client.create_collection(
        name=COLLECTION_NAME)

    documents_1, metadatas_1, ids_1 = prepare_mckinsey_data(DATA_PATH_1)
    documents_2, metadatas_2, ids_2 = prepare_accenture_data(DATA_PATH_2, ids_1)
    print(len(documents_1), len(metadatas_1), len(ids_1))
    print(len(documents_2), len(metadatas_2), len(ids_2))

    collection.add(
        documents=documents_1,
        metadatas=metadatas_1,
        ids=ids_1
    )
    collection.add(
        documents=documents_2,
        metadatas=metadatas_2,
        ids=ids_2
    )
    chroma_client.persist()
