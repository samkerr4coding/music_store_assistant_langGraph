import re

import numpy as np
import openai
from langchain_core.tools import tool



class VectorStoreRetriever:
    def __init__(self, doc: str, vectors: list, oai_client):
        self._arr = np.array(vectors)
        self._client = oai_client

    @classmethod
    def from_markdow(cls, oai_client):
        with open("policy.md", 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        embeddings = oai_client.embeddings.create(
            model="text-embedding-3-small", input=markdown_content
        )
        vectors = [emb.embedding for emb in embeddings.data]
        return cls(vectors, oai_client)

    def query(self, query: str, k: int = 5) -> list[dict]:
        embed = self._client.embeddings.create(
            model="text-embedding-3-small", input=[query]
        )
        # "@" is just a matrix multiplication in python
        scores = np.array(embed.data[0].embedding) @ self._arr.T
        top_k_idx = np.argpartition(scores, -k)[-k:]
        top_k_idx_sorted = top_k_idx[np.argsort(-scores[top_k_idx])]
        return [
            {**self._docs[idx], "similarity": scores[idx]} for idx in top_k_idx_sorted
        ]


retriever = VectorStoreRetriever.from_markdow(openai.Client())


@tool
def lookup_policy(query: str) -> str:
    """Consult the company policies to check whether certain options are permitted.
    Use this before making any flight changes performing other 'write' events."""
    docs = retriever.query(query, k=2)
    return "\n\n".join([doc["page_content"] for doc in docs])
