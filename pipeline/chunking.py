def chunk_text(text):
    sections = [s.strip() for s in text.split("\n\n") if s.strip()]
    chunks = []

    current_chunk = ""
    for section in sections:
        if len(current_chunk) + len(section) < 300:
            current_chunk += section + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = section + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks