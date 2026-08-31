from pipeline.metadata import add_metadata


def test_add_metadata_identifies_known_policy():
    chunks = [
        "Remote Work Policy\nEmployees may work remotely three days per week."
    ]

    enriched = add_metadata(chunks)

    assert enriched[0]["metadata"]["title"] == "Remote Work Policy"
    assert enriched[0]["metadata"]["source"] == "HR_DOC"
    assert enriched[0]["metadata"]["chunk_id"] == 0


def test_add_metadata_uses_unknown_for_unrecognized_content():
    chunks = ["Generic organizational information."]

    enriched = add_metadata(chunks)

    assert enriched[0]["metadata"]["title"] == "Unknown"


def test_add_metadata_preserves_original_text():
    text = "Employee Benefits Policy\nEmployees receive PTO."

    enriched = add_metadata([text])

    assert enriched[0]["text"] == text
