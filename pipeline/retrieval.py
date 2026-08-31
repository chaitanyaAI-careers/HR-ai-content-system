from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def build_index(embeddings):
    return np.array(embeddings)


def search_index(query_embedding, index, top_k=3):
    similarities = cosine_similarity([query_embedding], index)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    top_scores = similarities[top_indices]
    return top_scores, top_indices