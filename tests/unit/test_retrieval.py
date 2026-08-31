import numpy as np

from pipeline.retrieval import build_index, search_index


def test_build_index_returns_numpy_array():
    embeddings = [
        [1.0, 0.0],
        [0.0, 1.0],
    ]

    index = build_index(embeddings)

    assert isinstance(index, np.ndarray)
    assert index.shape == (2, 2)


def test_search_index_returns_most_similar_item_first():
    index = build_index(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [0.8, 0.2],
        ]
    )

    scores, indices = search_index(
        query_embedding=[1.0, 0.0],
        index=index,
        top_k=2,
    )

    assert indices[0] == 0
    assert len(indices) == 2
    assert scores[0] >= scores[1]


def test_search_index_respects_top_k():
    index = build_index(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [0.5, 0.5],
        ]
    )

    scores, indices = search_index(
        query_embedding=[1.0, 0.0],
        index=index,
        top_k=1,
    )

    assert len(scores) == 1
    assert len(indices) == 1
