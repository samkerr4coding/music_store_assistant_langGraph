import spacy
import numpy as np
from pathlib import Path
from langchain_core.tools import tool


class VectorStoreRetriever:
    def __init__(self, doc: str, vectors: np.ndarray, nlp):
        self._arr = vectors
        self._nlp = nlp
        self._docs = doc

    @classmethod
    def from_markdown(cls):
        # Load the spaCy model
        nlp = spacy.load("en_core_web_md")

        print(Path.cwd())
        # Read the markdown file
        with open("./tools/policy.md", 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Create embeddings for the markdown content
        lines = markdown_content.split("\n")
        embeddings = []
        for line in lines:
            doc = nlp(line)
            if doc.vector.size:  # Ensure the vector is not empty
                embeddings.append(doc.vector)

        # Convert list of vectors to numpy array
        vectors = np.array(embeddings)
        print("Success")
        return cls(markdown_content, vectors, nlp)

    def query(self, query: str, k: int = 5) -> list[dict]:
        # Generate embeddings for the query using spaCy
        query_embedding = self._nlp(query).vector

        # Compute similarity scores
        scores = np.dot(self._arr, query_embedding)

        # Get top-k most similar results
        top_k_idx = np.argpartition(scores, -k)[-k:]
        top_k_idx_sorted = top_k_idx[np.argsort(-scores[top_k_idx])]

        return [{"page_content": self._docs.split("\n")[idx], "similarity": scores[idx]} for idx in top_k_idx_sorted]


# Initialize the retriever with spaCy embeddings
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
