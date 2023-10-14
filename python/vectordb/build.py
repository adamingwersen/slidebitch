import os
import json
import chromadb
from chromadb.config import Settings
from openai_embedding_function import get_openai_ef

from pprint import pprint as pp
from dotenv import load_dotenv

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
PERSIST_DIRECTORY = os.getenv("PERSIST_DIR")
DATA_PATH = "../scrape/mckinsey/data/content.json"


def prepare_data(path):
    with open(path, 'r') as f:
        data = json.load(f)
    documents = [''.join(doc['paragraphs']) for doc in data]
    metadatas = [{'title': doc['title'], 'description': ''.join(doc['description']),
                  'link': doc['link']} for doc in data]
    ids = [str(i) for i in range(len(data))]
    print(len(documents), len(metadatas), len(ids))
    return documents, metadatas, ids


if __name__ == "__main__":
    load_dotenv()
    openai_ef = get_openai_ef(os.getenv("OPENAI_API_KEY"))
    chroma_client = chromadb.Client(
        Settings(persist_directory=PERSIST_DIRECTORY, chroma_db_impl="duckdb+parquet"))
    chroma_client.delete_collection(name=COLLECTION_NAME)
    collection = chroma_client.create_collection(
        name=COLLECTION_NAME)

    documents, metadatas, ids = prepare_data(DATA_PATH)
    print(len(documents), len(metadatas), len(ids))

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    chroma_client.persist()
