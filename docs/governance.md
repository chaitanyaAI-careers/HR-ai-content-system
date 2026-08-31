# Governance

## Purpose

The governance layer explores how retrieval systems can protect sensitive information while preserving useful access to enterprise knowledge.

The current implementation focuses on deterministic redaction and role-conditioned output behavior using a synthetic HR policy corpus.

## Current Governance Flow

```text
Retrieved Evidence
        |
        v
Identify User Role
        |
        +-------------------+
        |                   |
        v                   v
    Employee                HR
        |                   |
        v                   v
Sensitive-Data          Original
Redaction               Evidence
        |                   |
        +---------+---------+
                  |
                  v
          Governed Result
```

## Implemented Protection

`pipeline/governance.py` provides deterministic protection for selected sensitive information.

Current redaction includes:

* SSN patterns such as `123-45-6789`
* the term `SSN`
* the term `salary`
* case-insensitive sensitive-term matching

For the `employee` role, these values are redacted before retrieved evidence is returned.

For the `hr` role, the retrieved text is currently preserved.

## Terminology Boundary

The current implementation is best described as:

**role-conditioned redaction**

It is not yet a complete role-based access control system.

A production RBAC implementation would additionally require capabilities such as:

* authenticated user identities
* explicit roles and permissions
* document-level access policies
* authorization checks before retrieval
* deny-by-default behavior
* policy enforcement
* access audit records
* administrative role management

These capabilities are planned but are not represented as implemented features in the current repository.

## Why Governance Happens Near Retrieval

Sensitive information can enter an AI system through retrieved context even when the final response layer is otherwise well controlled.

A governed retrieval architecture therefore needs to consider protection before retrieved evidence is exposed downstream.

The target direction is:

```text
User Identity
      |
      v
Authorization Policy
      |
      v
Permitted Document Set
      |
      v
Retrieval
      |
      v
Sensitive-Data Filtering
      |
      v
Grounded Response
      |
      v
Audit Record
```

## Synthetic Data

The repository uses synthetic HR policy content.

It is not intended to contain:

* real employee identities
* real SSNs
* payroll records
* private resumes
* healthcare records
* customer HR information

This allows governance behavior to be tested without exposing production personnel data.

## Testing

Current automated governance tests verify:

* SSN pattern removal
* sensitive-term redaction
* case-insensitive redaction
* employee-role redaction behavior
* HR-role preservation behavior

These tests provide executable evidence for the currently implemented governance controls.

## Planned Governance Evaluation

Future evaluation will compare:

```text
Standard Retrieval
        vs
PII-Filtered Retrieval
        vs
PII + Authorization-Aware Retrieval
```

The benchmark will measure both utility and protection.

Target governance metrics include:

* sensitive-data leakage rate
* unauthorized retrieval rate
* access-denial correctness
* false-denial rate
* retrieval-quality impact
* answer usefulness

## Planned Improvements

* explicit authorization policy model
* true role-based document filtering
* policy-aware retrieval
* unauthorized-query test cases
* richer synthetic sensitive-data corpus
* PII leakage regression tests
* audit events for governance decisions
* reproducible governance benchmark reports

## Design Principle

The project treats governance as part of the retrieval architecture rather than as a final-response-only filter.

The long-term goal is to evaluate whether enterprise retrieval systems can remain useful while enforcing measurable privacy and access constraints.
