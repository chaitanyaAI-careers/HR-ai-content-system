from pipeline.evaluation import evaluate_system


def test_evaluation_returns_all_golden_questions():
    def query_fn(question):
        return "No confident answer found in the HR knowledge base."

    results, accuracy = evaluate_system(query_fn)

    assert len(results) == 21
    assert 0.0 <= accuracy <= 1.0


def test_evaluation_marks_matching_answer_correct():
    def query_fn(question):
        if question == "How many PTO days do employees get?":
            return [{"text": "Employees receive 20 days of PTO."}]

        return "No confident answer found in the HR knowledge base."

    results, _ = evaluate_system(query_fn)

    target = next(
        item
        for item in results
        if item["question"] == "How many PTO days do employees get?"
    )

    assert target["correct"] is True


def test_irrelevant_query_is_correct_when_system_declines():
    def query_fn(question):
        return "No confident answer found in the HR knowledge base."

    results, _ = evaluate_system(query_fn)

    target = next(
        item
        for item in results
        if item["question"] == "What is the weather today?"
    )

    assert target["correct"] is True
