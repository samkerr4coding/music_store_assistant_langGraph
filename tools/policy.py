import numpy as np
import re
from langchain_core.tools import tool
from langchain_ollama import OllamaEmbeddings

class VectorStoreRetriever:
    def __init__(self, docs: list, vectors: list, ollama_client):
        self._docs = docs
        self._arr = np.array(vectors).astype("float32")
        self._client = ollama_client

    @classmethod
    def from_markdown(cls, ollama_client):
        # Read the markdown file
        with open("./tools/policy.md", 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Split markdown content into sections
        sections = markdown_content.split("\n")

        # Generate embeddings for the document sections
        embeddings = cls._embed_text(sections, ollama_client)
        vectors = [embedding for embedding in embeddings]  # Flatten the list of lists

        return cls(sections, vectors, ollama_client)

    @staticmethod
    def _embed_text(text_list, ollama_client):
        # Generate embeddings using Ollama client
        embeddings = ollama_client.embed_documents(text_list)
        return embeddings

    def query(self, query: str, k: int = 5) -> list[dict]:
        # Generate embedding for the query
        query_embedding = self._client.embed_documents([query])[0]

        # Calculate scores using matrix multiplication
        scores = np.array(query_embedding) @ self._arr.T

        # Get top k indices
        top_k_idx = np.argpartition(scores, -k)[-k:]
        top_k_idx_sorted = top_k_idx[np.argsort(-scores[top_k_idx])]

        # Return the most relevant documents
        return [
            {**self._docs[idx], "similarity": scores[idx]} for idx in top_k_idx_sorted
        ]

# Initialize the Ollama client
ollama_client = OllamaEmbeddings(model="nomic-embed-text")

# Initialize the retriever with documents and embeddings
retriever = VectorStoreRetriever.from_markdown(ollama_client)

@tool
def lookup_policy(query: str) -> str:
    """Consult the company policies to check whether certain options are permitted.
    Use this before making any flight changes performing other 'write' events."""
    docs = retriever.query(query, k=2)
    return "\n\n".join([doc["page_content"] for doc in docs])
