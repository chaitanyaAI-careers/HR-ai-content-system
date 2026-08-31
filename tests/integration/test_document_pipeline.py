from pathlib import Path

from pipeline.chunking import chunk_text
from pipeline.ingestion import load_documents
from pipeline.metadata import add_metadata


def test_sample_document_pipeline():
    document_path = Path("data/sample_hr_docs.txt")

    text = load_documents(document_path)
    chunks = chunk_text(text)
    enriched = add_metadata(chunks)

    assert text
    assert chunks
    assert enriched
    assert len(enriched) == len(chunks)

    titles = {
        item["metadata"]["title"]
        for item in enriched
    }

    assert "Employee Benefits Policy" in titles
