# Evaluation

## Purpose

Evaluation is a core part of HR AI Content System.

The project is designed not only to retrieve HR information, but also to measure whether retrieval behavior is useful, grounded, safe, and appropriate for enterprise settings.

The current implementation includes a lightweight golden-question evaluation and automated tests. Future work will expand this into formal retrieval and governance benchmarking.

## Current Evaluation

`pipeline/evaluation.py` contains a small golden set of HR and non-HR questions.

The current dataset includes questions covering topics such as:

* PTO
* PTO carryover
* parental leave
* sick leave
* remote work
* confidentiality
* benefits enrollment
* leave approval
* termination
* employee-data handling

It also includes unrelated questions such as:

* company stock price
* CEO identity
* weather
* jokes
* cryptocurrency prices

These unrelated questions help test whether the system declines queries that are not supported by the HR knowledge base.

## Current Evaluation Logic

The current evaluator:

1. sends each golden question to a supplied query function,
2. examines the returned response,
3. checks for an expected answer signal,
4. checks refusal behavior for unsupported questions,
5. records whether each item passed,
6. calculates aggregate accuracy.

This is intentionally a lightweight evaluation method.

It should not be interpreted as a complete retrieval benchmark.

## Current Test Coverage

The repository currently includes 17 automated tests across unit and integration layers.

Test areas include:

* document chunking
* metadata enrichment
* sensitive-data redaction
* role-conditioned governance behavior
* vector index construction
* cosine-similarity search
* top-k retrieval behavior
* golden-question evaluation
* irrelevant-query handling
* document preparation integration

Run the automated test suite with:

```bash
python3 -m pytest
```

## Evaluation Boundary

The existing evaluator uses expected substring signals rather than formal information-retrieval metrics.

For example, a PTO question may be considered correct when the retrieved response contains an expected value such as `20`.

This provides useful regression evidence for a small prototype, but it does not measure retrieval ranking quality comprehensively.

The repository therefore does not currently claim implemented support for:

* Recall@K
* Precision@K
* MRR
* NDCG
* MAP
* groundedness scoring
* citation correctness scoring
* authorization accuracy
* PII leakage rate

These metrics are part of the planned evaluation expansion.

## Target Retrieval Benchmark

The next evaluation layer will use a larger synthetic corpus and a structured golden dataset containing:

```text
Question
    |
    +--> Expected relevant document IDs
    |
    +--> Expected answer evidence
    |
    +--> Required access role
    |
    +--> Sensitive-data expectations
```

This will allow retrieval behavior to be evaluated independently from answer formatting.

## Planned Retrieval Metrics

### Recall@K

Measures whether relevant evidence appears within the top K retrieved results.

This will answer questions such as:

> Did the system retrieve the correct HR policy within the first 3 or 5 results?

### Mean Reciprocal Rank

MRR will measure how early the first relevant result appears in the ranking.

Higher values indicate that relevant evidence is surfaced closer to rank one.

### NDCG

Normalized Discounted Cumulative Gain will be used when the benchmark contains graded relevance judgments.

This provides a stronger ranking-quality signal than simple accuracy.

## Governance Evaluation

The distinctive evaluation direction for this project is the comparison of retrieval quality and governance behavior together.

The planned experiment is:

```text
Standard Retrieval
        vs
PII-Filtered Retrieval
        vs
PII + Authorization-Aware Retrieval
```

The purpose is to measure whether stronger governance controls reduce sensitive-data exposure without unnecessarily damaging retrieval usefulness.

## Planned Governance Metrics

### Sensitive-Data Leakage Rate

Measures how often protected information is exposed when policy requires that it remain hidden.

### Access-Denial Correctness

Measures whether users are denied information they are not authorized to retrieve.

### False-Denial Rate

Measures whether authorized information is incorrectly withheld.

### Retrieval Quality Under Governance

Compares retrieval metrics before and after governance policies are applied.

This helps identify whether privacy or authorization controls materially reduce retrieval effectiveness.

## Regression Evaluation

Future benchmark runs should be reproducible so retrieval changes can be compared over time.

The target workflow is:

```text
Code / Model / Retrieval Change
            |
            v
Run Golden Benchmark
            |
            v
Calculate Retrieval Metrics
            |
            v
Calculate Governance Metrics
            |
            v
Compare Against Baseline
            |
            v
Generate Evaluation Report
```

A regression should be visible when a change causes:

* lower Recall@K
* lower MRR or NDCG
* higher sensitive-data leakage
* incorrect access decisions
* degraded irrelevant-query handling

## Reproducibility Goals

Future evaluation work will include:

* versioned synthetic datasets
* versioned golden questions
* deterministic benchmark configuration where possible
* machine-readable evaluation output
* human-readable benchmark reports
* baseline comparisons
* CI-compatible evaluation checks

## Research Question

The broader research question is:

> How can enterprise retrieval systems improve knowledge access while preserving measurable privacy, authorization, and grounding guarantees?

The project will use controlled synthetic experiments to study the trade-off between retrieval utility and governance strength.

## Current Status

Implemented today:

* small golden-question dataset
* expected-answer signal checks
* unsupported-query refusal checks
* aggregate accuracy
* automated unit and integration testing

In development:

* formal retrieval metrics
* larger synthetic corpus
* larger golden dataset
* governance-specific metrics
* retrieval regression benchmarks
* reproducible evaluation reports
