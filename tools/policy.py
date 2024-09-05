import re
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_core.tools import tool
import ollama  # Assuming Ollama's Python client is available


class VectorStoreRetriever:
    def __init__(self, doc: str, vectors: list, model):
        self._arr = np.array(vectors)
        self._model = model
        self._docs = doc  # You might want to keep a reference to the original document

    @classmethod
    def from_markdown(cls, model_name="all-MiniLM-L6-v2"):
        # Load the local embedding model
        model = SentenceTransformer(model_name)

        print(Path.cwd())
        # Read the markdown file
        with open("./tools/policy.md", 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Create embeddings for the markdown content
        embeddings = model.encode(markdown_content.split("\n"))  # Split by lines for better granularity
        vectors = np.array(embeddings)
        return cls(markdown_content, vectors, model)

    def query(self, query: str, k: int = 5) -> list[dict]:
        # Generate embeddings for the query using the local model
        query_embedding = self._model.encode([query])

        # Compute similarity scores
        scores = np.dot(query_embedding, self._arr.T)

        # Get top-k most similar results
        top_k_idx = np.argpartition(scores[0], -k)[-k:]
        top_k_idx_sorted = top_k_idx[np.argsort(-scores[0][top_k_idx])]

        return [{"page_content": self._docs.split("\n")[idx], "similarity": scores[0][idx]} for idx in top_k_idx_sorted]


# Initialize the retriever with local embeddings
retriever = VectorStoreRetriever.from_markdown()


# Define the tool with Ollama integration
@tool
def lookup_policy(query: str) -> str:
    """Consult the company policies to check whether certain options are permitted.
    Use this before making any flight changes or performing other 'write' events."""

    # Use the local retriever to get the relevant parts of the document
    docs = retriever.query(query, k=2)

    # Combine the results into a single response
    return "\n\n".join([doc["page_content"] for doc in docs])
