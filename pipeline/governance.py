import re


def redact_pii(text):
    text = re.sub(
        r"\b\d{3}-\d{2}-\d{4}\b",
        "[REDACTED_SSN]",
        text,
    )

    text = re.sub(
        r"\bSSN\b",
        "[REDACTED]",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r"\bsalary\b",
        "[REDACTED]",
        text,
        flags=re.IGNORECASE,
    )

    return text


def apply_rbac(results, role="employee"):
    filtered = []

    for result in results:
        text = result["text"]

        if role == "employee":
            text = redact_pii(text)

        filtered.append(
            {
                "score": result["score"],
                "text": text,
                "metadata": result["metadata"],
            }
        )

    return filtered
