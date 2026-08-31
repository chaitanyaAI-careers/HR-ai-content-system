# HR AI Content System

**Governed Enterprise AI Retrieval · PII Protection · Evaluation**

HR AI Content System is a Python-based retrieval and governance project exploring how enterprise knowledge systems can combine semantic retrieval, sensitive-data protection, role-aware behavior, grounding, and measurable evaluation.

The project uses a synthetic HR policy corpus so retrieval and governance behavior can be demonstrated without exposing real employee data.

## Why This Project Exists

Enterprise AI systems need to do more than retrieve relevant information. They also need to consider:

* whether retrieved information contains sensitive data
* how system behavior should differ by user role
* whether responses are grounded in approved knowledge
* whether unrelated questions should be rejected
* whether retrieval and governance behavior can be evaluated reproducibly

This project provides a compact environment for developing and testing those concepts.

## Architecture

```text
Synthetic HR Documents
        |
        v
Document Ingestion
        |
        v
Section / Length-Based Chunking
        |
        v
Metadata Enrichment
        |
        v
SentenceTransformer Embeddings
        |
        v
Cosine-Similarity Retrieval
        |
        v
Role-Conditioned Redaction
        |
        v
Confidence / Relevance Checks
        |
        v
Grounded Extractive Answer
        |
        v
Source Attribution
```

## Implemented

### Document Processing

* text document ingestion
* section and length-based chunk construction
* chunk-level metadata
* policy-title classification
* source and chunk traceability

### Semantic Retrieval

* SentenceTransformer embeddings
* `all-MiniLM-L6-v2`
* NumPy vector-index representation
* cosine-similarity ranking
* configurable top-k retrieval

### Governance

* deterministic SSN-pattern redaction
* sensitive-term redaction
* case-insensitive sensitive-term handling
* role-conditioned result transformation
* separate employee and HR behavior

The current role logic is **role-conditioned redaction**, not a complete enterprise RBAC or authorization implementation.

### Grounded Response Behavior

* answers derived from retrieved HR policy content
* source attribution
* similarity-based confidence checks
* rejection of low-confidence questions
* handling of unrelated queries

The current answer layer is extractive and deterministic. It does not currently use an LLM for response generation.

### Evaluation

A small golden-question dataset evaluates:

* relevant HR questions
* expected answer signals
* irrelevant questions
* safe refusal behavior

The existing evaluation is intentionally lightweight and will be expanded into formal retrieval and governance benchmarking.

## Testing

The project includes unit and integration tests covering:

* chunking
* metadata enrichment
* PII redaction
* role-conditioned governance
* vector index construction
* cosine-similarity retrieval
* golden-question evaluation
* document preparation pipeline

Current test suite:

**17 automated tests**

Run:

```bash
python3 -m pytest
```

The Career repository runs this test suite through GitHub Actions CI.

## Synthetic Dataset

`data/sample_hr_docs.txt` contains synthetic HR policies covering:

* PTO
* parental leave
* sick leave
* remote work
* confidentiality
* benefits enrollment
* manager approvals
* termination
* employee-data privacy

No real employee records are required by the example application.

## Project Structure

```text
HR-ai-content-system/
├── app.py
├── data/
│   └── sample_hr_docs.txt
├── docs/
├── pipeline/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── evaluation.py
│   ├── governance.py
│   ├── ingestion.py
│   ├── metadata.py
│   └── retrieval.py
├── scripts/
│   ├── setup.sh
│   └── smoke_test.sh
├── tests/
│   ├── integration/
│   └── unit/
├── pytest.ini
├── requirements.txt
└── README.md
```

## Technology Stack

* Python
* Gradio
* Sentence Transformers
* NumPy
* scikit-learn
* pytest

## Research Direction

The next research question is:

> How does governance affect enterprise retrieval quality, sensitive-data leakage risk, and authorization correctness?

The planned benchmark compares:

```text
Standard Retrieval
        vs
PII-Filtered Retrieval
        vs
PII + Authorization-Aware Retrieval
```

Target metrics include:

* Recall@K
* MRR
* NDCG
* sensitive-data leakage rate
* access-denial correctness
* answer usefulness
* retrieval regression performance

## In Development

* document-level authorization policies
* true RBAC-aware retrieval filtering
* larger synthetic HR corpus
* expanded golden dataset
* Recall@K, MRR, and NDCG evaluation
* PII leakage tests
* authorization-denial tests
* retrieval regression tests
* reproducible benchmark reports
* Docker

## Engineering Focus

This project demonstrates practical work in:

* enterprise AI retrieval
* responsible AI engineering
* PII protection
* semantic search
* evaluation engineering
* golden datasets
* grounded knowledge systems
* governance-oriented testing

## Repository Safety

This repository uses synthetic example HR content and is not intended to contain:

* production employee records
* real SSNs
* payroll data
* private resumes
* customer HR databases
* production credentials

## Status

Active supporting and research project focused on:

**Governed Enterprise AI Retrieval + Evaluation**
