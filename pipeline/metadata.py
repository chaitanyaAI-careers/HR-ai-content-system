def add_metadata(chunks):
    enriched = []

    for i, chunk in enumerate(chunks):
        title = "Unknown"
        if "Employee Benefits Policy" in chunk:
            title = "Employee Benefits Policy"
        elif "Parental Leave Policy" in chunk:
            title = "Parental Leave Policy"
        elif "Sick Leave Policy" in chunk:
            title = "Sick Leave Policy"
        elif "Remote Work Policy" in chunk:
            title = "Remote Work Policy"
        elif "Confidentiality Policy" in chunk:
            title = "Confidentiality Policy"
        elif "Code of Conduct" in chunk:
            title = "Code of Conduct"
        elif "Benefits Enrollment" in chunk:
            title = "Benefits Enrollment"
        elif "Manager Approval Policy" in chunk:
            title = "Manager Approval Policy"
        elif "Termination Policy" in chunk:
            title = "Termination Policy"
        elif "Data Privacy Policy" in chunk:
            title = "Data Privacy Policy"

        metadata = {
            "chunk_id": i,
            "title": title,
            "length": len(chunk),
            "source": "HR_DOC"
        }

        enriched.append({
            "text": chunk,
            "metadata": metadata
        })

    return enriched