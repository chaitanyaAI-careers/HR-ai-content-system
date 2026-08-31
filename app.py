import gradio as gr

from pipeline.ingestion import load_documents
from pipeline.chunking import chunk_text
from pipeline.metadata import add_metadata
from pipeline.embeddings import generate_embeddings, model
from pipeline.retrieval import build_index, search_index
from pipeline.governance import apply_rbac
from pipeline.evaluation import evaluate_system


SIMILARITY_THRESHOLD = 0.20


def retrieve_results(query, role="employee"):
    text = load_documents("data/sample_hr_docs.txt")
    chunks = chunk_text(text)
    enriched = add_metadata(chunks)

    embeddings = generate_embeddings(enriched)
    index = build_index(embeddings)

    query_embedding = model.encode(query)
    scores, indices = search_index(query_embedding, index, top_k=3)

    results = []
    for score, idx in zip(scores, indices):
        results.append({
            "score": float(score),
            "text": enriched[idx]["text"],
            "metadata": enriched[idx]["metadata"]
        })

    results = apply_rbac(results, role=role)
    return results


def generate_answer(results):
    if not results:
        return "No results found."

    top_result = results[0]
    text = top_result["text"]
    score = top_result["score"]
    source = top_result["metadata"].get("title", "HR Document")

    if score < SIMILARITY_THRESHOLD:
        return "No confident answer found in the HR knowledge base."

    if score < 0.30:
        return "This question appears to be outside the HR knowledge base. Please ask an HR-related question."

    sentences = [s.strip() for s in text.split(".") if s.strip()]
    short_answer = ". ".join(sentences[:2]).strip()

    return (
        f"Answer: {short_answer}\n\n"
        f"Source: {source}\n"
        f"Confidence: {score:.2f}"
    )


def process_and_query(query, role):
    results = retrieve_results(query, role=role)
    return generate_answer(results)


def run_evaluation():
    eval_results, accuracy = evaluate_system(
        lambda q: retrieve_results(q, role="employee")
    )

    output = ""
    for r in eval_results:
        output += (
            f"Question: {r['question']}\n"
            f"Expected: {r['expected']}\n"
            f"Correct: {r['correct']}\n"
            f"{'-' * 50}\n"
        )

    output += f"\nOverall Accuracy: {accuracy * 100:.2f}%"
    return output


with gr.Blocks() as demo:
    gr.Markdown("# HR AI Content Optimization System")
    gr.Markdown(
        "AI-ready HR knowledge pipeline with retrieval, governance, and evaluation."
    )

    with gr.Tab("Query System"):
        query_input = gr.Textbox(label="Ask an HR Question")
        role_input = gr.Radio(
            choices=["employee", "hr"],
            value="employee",
            label="User Role"
        )
        query_output = gr.Textbox(label="Answer", lines=15)
        query_btn = gr.Button("Search")

        query_btn.click(
            process_and_query,
            inputs=[query_input, role_input],
            outputs=query_output
        )

    with gr.Tab("Evaluation"):
        eval_btn = gr.Button("Run Evaluation")
        eval_output = gr.Textbox(label="Evaluation Results", lines=20)

        eval_btn.click(run_evaluation, outputs=eval_output)

demo.launch()