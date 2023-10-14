from chromadb.utils import embedding_functions


def get_openai_ef(OPENAI_API_KEY):
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=OPENAI_API_KEY,
        model_name="text-embedding-ada-002"
    )
    return openai_ef
