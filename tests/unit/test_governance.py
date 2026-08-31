from pipeline.governance import apply_rbac, redact_pii


def test_redact_pii_removes_ssn_pattern():
    text = "Employee SSN is 123-45-6789."

    redacted = redact_pii(text)

    assert "123-45-6789" not in redacted
    assert "[REDACTED_SSN]" in redacted


def test_redact_pii_redacts_sensitive_terms():
    text = "SSN and salary information must remain protected."

    redacted = redact_pii(text)

    assert "SSN" not in redacted
    assert "salary" not in redacted.lower()


def test_employee_role_receives_redacted_results():
    results = [
        {
            "score": 0.9,
            "text": "Salary information includes SSN 123-45-6789.",
            "metadata": {"title": "Confidentiality Policy"},
        }
    ]

    filtered = apply_rbac(results, role="employee")

    assert "123-45-6789" not in filtered[0]["text"]
    assert "salary" not in filtered[0]["text"].lower()


def test_hr_role_preserves_original_result_text():
    results = [
        {
            "score": 0.9,
            "text": "Salary information is restricted.",
            "metadata": {"title": "Confidentiality Policy"},
        }
    ]

    filtered = apply_rbac(results, role="hr")

    assert filtered[0]["text"] == results[0]["text"]
