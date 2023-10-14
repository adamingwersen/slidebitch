from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv
from peek import find_formatted
import json
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
PERSIST_DIRECTORY = os.getenv("PERSIST_DIR")
chroma_client = chromadb.Client(Settings(
    persist_directory=PERSIST_DIRECTORY, chroma_db_impl="duckdb+parquet",))
collection = chroma_client.get_collection(
    name=COLLECTION_NAME)


class QueryInput(BaseModel):
    collection: str = 'mckinsey'
    querystring: str
    n_results: int = 5


class CollectionMetadata(BaseModel):
    description: str
    link: str
    title: str


class QueryOutput(BaseModel):
    distance: float
    id: str
    metadata: CollectionMetadata


@app.api_route('/query', methods=['POST', 'HEAD', 'OPTIONS'])
async def get_response(query: QueryInput) -> list[QueryOutput]:
    print(query.querystring)
    query_result = find_formatted(collection, query.querystring)
    return query_result
