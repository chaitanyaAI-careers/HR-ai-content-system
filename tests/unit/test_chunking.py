from pipeline.chunking import chunk_text


def test_chunk_text_returns_nonempty_chunks():
    text = (
        "Policy A\n\n"
        "Employees receive paid leave.\n\n"
        "Policy B\n\n"
        "Remote work requires approval."
    )

    chunks = chunk_text(text)

    assert chunks
    assert all(chunk.strip() for chunk in chunks)


def test_chunk_text_preserves_content():
    text = "Policy A\n\nEmployees receive paid leave."

    chunks = chunk_text(text)

    combined = "\n".join(chunks)

    assert "Policy A" in combined
    assert "Employees receive paid leave." in combined


def test_chunk_text_handles_empty_input():
    assert chunk_text("") == []
