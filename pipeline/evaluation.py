def evaluate_system(query_fn):
    golden_set = [
        {"question": "How many PTO days do employees get?", "expected": "20"},
        {"question": "Can PTO be carried over?", "expected": "carry"},
        {"question": "How many PTO carryover days?", "expected": "5"},
        {"question": "How long is parental leave?", "expected": "12"},
        {"question": "Who approves parental leave?", "expected": "hr"},
        {"question": "How many sick leave days are given?", "expected": "10"},
        {"question": "Does sick leave carry over?", "expected": "not"},
        {"question": "How many days can employees work remotely?", "expected": "3"},
        {"question": "Who approves remote work?", "expected": "manager"},
        {"question": "What sensitive information should not be shared?", "expected": "personal"},
        {"question": "Is salary confidential?", "expected": "salary"},
        {"question": "When should employees enroll in benefits?", "expected": "30"},
        {"question": "What behavior is expected from employees?", "expected": "professional"},
        {"question": "Who approves leave requests?", "expected": "manager"},
        {"question": "How much notice is required before resignation?", "expected": "2"},
        {"question": "How should employee data be handled?", "expected": "secure"},

        {"question": "What is the company stock price?", "expected": "none"},
        {"question": "Who is the CEO?", "expected": "none"},
        {"question": "What is the weather today?", "expected": "none"},
        {"question": "Tell me a joke", "expected": "none"},
        {"question": "What is bitcoin price?", "expected": "none"},
    ]

    results = []
    correct = 0

    for item in golden_set:
        response = query_fn(item["question"])

        if isinstance(response, list) and response:
            answer_text = response[0]["text"].lower()
        else:
            answer_text = str(response).lower()

        if item["expected"] == "none":
            is_correct = "no confident answer" in answer_text
        else:
            is_correct = item["expected"] in answer_text

        if is_correct:
            correct += 1

        results.append({
            "question": item["question"],
            "expected": item["expected"],
            "correct": is_correct
        })

    accuracy = correct / len(golden_set)
    return results, accuracy