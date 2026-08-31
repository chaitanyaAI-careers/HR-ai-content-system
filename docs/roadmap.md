# Roadmap

## Project Direction

HR AI Content System is being developed as a focused research and engineering project for:

**Governed Enterprise AI Retrieval + Evaluation**

The project is intentionally narrower than a general-purpose RAG platform.

Its primary goal is to study and demonstrate how enterprise retrieval systems can balance:

* retrieval quality
* sensitive-data protection
* authorization
* grounding
* measurable evaluation

## Current Foundation

The current implementation provides:

* synthetic HR policy corpus
* text ingestion
* section and length-based chunking
* metadata enrichment
* SentenceTransformer embeddings
* cosine-similarity retrieval
* top-k ranking
* deterministic sensitive-data redaction
* role-conditioned behavior
* confidence-based irrelevant-query handling
* grounded extractive responses
* source attribution
* lightweight golden-question evaluation
* unit and integration testing

The automated test suite currently contains 17 tests.

## Phase 1 — Testing and Evaluation Foundation

Strengthen the existing prototype with recognizable evaluation infrastructure.

Planned work:

* expand the synthetic HR corpus
* move golden questions into versioned dataset files
* introduce explicit relevance judgments
* implement Recall@K
* implement Precision@K
* implement MRR
* implement NDCG
* add retrieval regression tests
* generate reproducible evaluation reports
* establish baseline retrieval results

Target outcome:

A retrieval system whose quality can be measured and compared across changes.

## Phase 2 — Governance Benchmark

Expand governance beyond deterministic redaction.

Planned work:

* create synthetic sensitive-data cases
* define protected information categories
* add PII leakage tests
* measure sensitive-data leakage rate
* measure false-redaction behavior
* compare retrieval behavior before and after filtering
* create governance regression tests

Target experiment:

```text
Standard Retrieval
        vs
PII-Filtered Retrieval
        vs
PII + Authorization-Aware Retrieval
```

Target outcome:

Quantifiable evidence showing how governance controls affect both safety and retrieval usefulness.

## Phase 3 — Authorization-Aware Retrieval

Replace the current role-conditioned redaction prototype with explicit authorization controls.

Planned work:

* authenticated identity abstraction
* formal role model
* permission model
* document-level access metadata
* authorization policy evaluation
* pre-retrieval document filtering
* deny-by-default behavior
* unauthorized-access test cases
* access-decision logging

Target architecture:

```text
User
  |
  v
Identity
  |
  v
Role / Permission Policy
  |
  v
Authorized Document Set
  |
  v
Retrieval
  |
  v
PII Protection
  |
  v
Grounded Response
```

Target outcome:

Actual authorization-aware retrieval rather than role-conditioned output filtering.

## Phase 4 — Retrieval Quality Improvements

Evaluate stronger retrieval strategies only after the baseline benchmark is reproducible.

Candidate experiments:

* improved chunking
* lexical retrieval
* BM25
* dense retrieval
* hybrid dense + lexical retrieval
* metadata filtering
* reranking
* query transformation

Each change should be measured against the same golden evaluation dataset.

Target outcome:

Evidence-based retrieval improvements rather than feature additions without benchmarks.

## Phase 5 — Reliability and Reproducibility

Improve engineering maturity around the research system.

Planned work:

* Docker
* reproducible local environment
* GitHub Actions CI
* automated test execution
* benchmark execution in CI
* structured evaluation output
* configuration validation
* deterministic benchmark settings where possible

Target outcome:

A project that can be cloned, tested, benchmarked, and reproduced consistently.

## Phase 6 — Research Report

Produce a reproducible comparison of retrieval governance strategies.

Primary research question:

> How do privacy and authorization controls affect retrieval quality, sensitive-data leakage, and access correctness in enterprise knowledge systems?

Candidate experiment dimensions:

* retrieval strategy
* redaction strategy
* authorization strategy
* user role
* corpus size
* query type

Primary metrics:

* Recall@K
* MRR
* NDCG
* sensitive-data leakage rate
* access-denial correctness
* false-denial rate
* answer usefulness

Target outcome:

A technical report supported by executable benchmark code and reproducible results.

## Explicit Non-Goals

This project is not intended to become another large general-purpose AI platform.

It does not need features simply to add technology keywords.

Unless justified by the research or engineering objective, the project should avoid unnecessary additions such as:

* unrelated autonomous agents
* generic MCP integrations
* GraphRAG without an evaluation hypothesis
* multiple vector databases solely for comparison
* complex distributed infrastructure without scale requirements

The project's strength should come from depth in retrieval governance and evaluation.

## Success Criteria

The project will be considered mature when it can demonstrate:

1. reproducible enterprise retrieval benchmarks,
2. measurable retrieval quality,
3. measurable sensitive-data leakage,
4. correct authorization behavior,
5. regression testing across retrieval changes,
6. clear evidence of governance-quality trade-offs,
7. reproducible execution through tests and CI,
8. documentation that distinguishes implemented features from planned research.

## Portfolio Position

Within the broader AI engineering portfolio, this project specializes in:

**Responsible AI · Enterprise Retrieval · PII Protection · Authorization · Evaluation · Benchmarking**

Its purpose is to provide deeper evidence in governance and research-oriented retrieval engineering rather than duplicate the responsibilities of larger AI platform projects.
