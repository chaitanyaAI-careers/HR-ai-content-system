# Architecture

## Purpose

HR AI Content System is a compact governed enterprise retrieval project designed to demonstrate how knowledge retrieval, sensitive-data handling, grounding, and evaluation can be combined in an AI-oriented information system.

The current implementation intentionally uses a synthetic HR policy corpus so the architecture can be evaluated without production employee data.

## System Flow

```text
Synthetic HR Policy Corpus
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
Vector Index
        |
        v
Cosine-Similarity Retrieval
        |
        v
Role-Conditioned Redaction
        |
        v
Confidence Thresholding
        |
        v
Grounded Extractive Response
        |
        v
Source Attribution
```

## Components

### Ingestion

`pipeline/ingestion.py`

Loads the source HR policy document from the local synthetic dataset.

### Chunking

`pipeline/chunking.py`

Groups document sections into bounded chunks.

The current implementation is section and length based. It should not be interpreted as semantic chunking.

### Metadata

`pipeline/metadata.py`

Adds retrieval metadata including:

* chunk identifier
* policy title
* chunk length
* source identifier

This provides basic traceability between retrieved evidence and source content.

### Embeddings

`pipeline/embeddings.py`

Uses the SentenceTransformers `all-MiniLM-L6-v2` model to create dense vector representations of HR content.

### Retrieval

`pipeline/retrieval.py`

Uses:

* NumPy for vector representation
* cosine similarity for ranking
* configurable top-k result selection

The current implementation is an in-memory retrieval prototype rather than a persistent production vector database.

### Governance

`pipeline/governance.py`

Applies deterministic redaction to selected sensitive information.

For the employee role, the current implementation redacts:

* SSN patterns
* SSN terminology
* salary terminology

The HR role currently receives the original retrieved text.

This is role-conditioned redaction. It is not yet a complete RBAC authorization system.

### Response Layer

`app.py`

The response layer:

* selects the highest-ranked evidence
* checks retrieval confidence
* rejects sufficiently low-confidence results
* derives a concise extractive answer
* exposes the originating policy title
* reports similarity confidence

No LLM is currently used for response generation.

### Evaluation

`pipeline/evaluation.py`

Contains a lightweight golden-question evaluation covering:

* expected HR questions
* expected answer signals
* unrelated questions
* refusal behavior

This provides a foundation for future formal retrieval and governance benchmarking.

## User Interface

The project uses Gradio to expose:

* HR question input
* role selection
* retrieved/grounded answers
* evaluation execution

## Testing Architecture

The automated test suite separates:

```text
tests/
├── unit/
└── integration/
```

Unit tests cover individual retrieval and governance components.

The integration test verifies document loading, chunking, and metadata enrichment across the document preparation pipeline.

## Current Design Boundary

The repository currently demonstrates a governed retrieval prototype.

It does not yet claim production implementations of:

* enterprise authentication
* complete RBAC authorization
* persistent vector storage
* distributed retrieval
* LLM generation
* production observability
* formal security controls

These boundaries are intentional and documented so implementation claims remain aligned with executable evidence.
