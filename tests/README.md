# Test Suite

## Overview
This directory contains automated unit and integration tests for the Multilingual Complaint Redressal System.

## Running Tests
Run pytest from the repository root:
```bash
pytest
```

To run only unit tests:
```bash
pytest tests/unit
```

## Test Structure
- `tests/unit/test_contract_schemas.py`: Validates that the Pydantic schemas in `nlp_engine` and `backend` strictly adhere to the contract defined in `docs/api_contract.md`.
- `tests/integration/`: End-to-end API tests and NLP pipeline integration tests.
