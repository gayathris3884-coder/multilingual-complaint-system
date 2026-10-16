# A Multilingual and Code-Mixed NLP Framework for Intelligent Understanding of Public-Service Complaints

## 1. Project Overview

In multilingual countries like India, citizens frequently submit civic grievances using a mix of languages—combining English, regional languages (Hindi, Marathi, Tamil, Bengali, etc.), and romanized code-mixed speech (e.g., *Hinglish* such as *"Pani ka pressure bohot low hai aur pipeline leak ho rahi hai"*).

Conventional keyword-matching or monolingual classification systems fail to parse such code-mixed, colloquial, or phonetically transliterated complaints. This results in misrouted tickets, severe resolution delays, and citizen frustration.

This project develops an **intelligent, end-to-end framework** capable of:
1. Parsing code-mixed and multilingual public service complaints.
2. Accurately classifying grievances into predefined municipal domains.
3. Generating concise administrative summaries.
4. Detecting duplicate complaints across geographic sectors.
5. Routing grievances to corresponding municipal departments with a human-in-the-loop review mechanism.

---

## 2. Key Features

- **Multilingual & Code-Mixed Understanding**: Handles pure English, native scripts (Devanagari, etc.), and code-mixed Romanized text (e.g., Hinglish).
- **Automated Categorization**: Maps complaints into 6 standard categories:
  - `water_supply`
  - `road_damage`
  - `garbage`
  - `drainage`
  - `streetlight`
  - `other`
- **Confidence Scoring & Human-in-the-Loop Review**: Automatically flags ambiguous or low-confidence predictions (`requires_human_review: true`) for manual officer verification.
- **Deduplication & Clustering**: Identifies semantic duplicates submitted by multiple residents for the same incident or area.
- **Actionable Summarization**: Condenses lengthy or colloquial complaints into standardized administrative summaries.
- **Citizen Portal & Municipal Officer Dashboard**: Clean, responsive interfaces for grievance filing and department triage.

---

## 3. Proposed Technology Stack

| Layer | Technology | Rationale |
|---|---|---|
| **Frontend** | React (Vite) + Vanilla CSS | High performance, modular component architecture, lightweight bundle, rich interactive dashboard |
| **Backend API** | Python 3.10+ & FastAPI | Asynchronous processing, native OpenAPI documentation, strict Pydantic contract validation |
| **Database** | SQLite (Development) | Zero-setup, portable, SQL-standard relational storage (easily migratable to PostgreSQL) |
| **NLP Engine** | Python, Hugging Face Transformers / Indic NLP | Specialized architectures for multilingual & Indic text processing (e.g., IndicBERT, MuRIL, XLM-RoBERTa, Sentence-Transformers) |
| **Testing** | Pytest, HTTPX | Automated unit, schema, and integration tests |

---

## 4. Team Division & Member Responsibilities

This college project is divided equally between two core members with clearly separated responsibilities:

```
┌────────────────────────────────────────────────────────┐
│                   Shared API Contract                  │
│                (docs/api_contract.md)                  │
└───────────────────────────┬────────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│        MEMBER 1         │     │        MEMBER 2         │
│     NLP Engine Core     │     │ Application & Platform  │
└─────────────────────────┘     └─────────────────────────┘
```

### Member 1: NLP Engine & Intelligent Processing
- **Language & Script Identification**: Detect source language and romanized code-mixed patterns (e.g., `hi-Latn`).
- **Text Normalization & Preprocessing**: Handle phonetic variations, colloquial spellings, noise removal, and tokenization.
- **Categorization Model**: Develop and train/fine-tune models to classify grievances into the 6 standardized category IDs with confidence scoring.
- **Grievance Summarization**: Implement extractive/abstractive summarization logic to generate canonical descriptions.
- **Duplicate Detection**: Implement semantic embeddings and similarity metrics to flag redundant tickets.
- **NLP Evaluation & Benchmarking**: Measure Precision, Recall, F1-score across code-mixed test samples.

### Member 2: Application, Backend, Database, Routing & Dashboard
- **Backend Architecture**: Implement FastAPI services, request routing, validation middleware, and API contract enforcement.
- **Database Engineering**: Design relational SQLite schemas (Complaints, Departments, Citizens, Audit Logs) and ORM models.
- **Department Routing Engine**: Logic to assign tickets to relevant civic departments based on category, ward, and urgency.
- **Administrative Dashboard**: Build the React dashboard for municipal officers to view, filter, review, and resolve complaints.
- **Citizen Submission Portal**: Build an accessible, clean submission interface with live status tracking.
- **System Integration & Testing**: Orchestrate end-to-end integration between the frontend, backend, database, and NLP engine.

---

## 5. Repository Structure

```
multilingual-complaint-system/
├── .env.example              # Development environment variable template
├── .gitignore                # Git ignore rules for Python, Node, DB, and models
├── README.md                 # Project master documentation
├── docs/                     # Architectural specs, API contracts, guides
│   ├── api_contract.md       # Shared API payload contracts & endpoints
│   └── architecture.md       # System high-level design
├── dataset/                  # Dataset storage and annotation guidelines
│   ├── raw/                  # Raw code-mixed & multilingual data
│   ├── processed/            # Cleaned, tokenized, annotated datasets
│   └── README.md             # Dataset acquisition & annotation guidelines
├── nlp_engine/               # [Member 1] NLP models, pipelines, preprocessing
│   ├── schemas.py            # Pydantic schemas for NLP inputs and outputs
│   ├── constants.py          # Category IDs and language definitions
│   ├── pipeline/             # Tokenization, categorization, deduplication logic
│   ├── requirements.txt      # NLP specific dependencies
│   └── README.md             # NLP engine architecture and instructions
├── backend/                  # [Member 2] FastAPI service, database, routing
│   ├── app/
│   │   ├── main.py           # FastAPI entrypoint
│   │   ├── core/             # Configuration & security settings
│   │   ├── db/               # Database connection and session management
│   │   ├── models/           # SQLAlchemy / relational database models
│   │   ├── schemas/          # API request and response models
│   │   └── api/v1/           # API route handlers
│   ├── requirements.txt      # Backend dependencies
│   └── README.md             # Backend setup and run instructions
├── frontend/                 # [Member 2] React + Vite citizen portal & dashboard
│   ├── src/                  # Components, pages, styles
│   ├── package.json          # Frontend dependencies & scripts
│   └── README.md             # Frontend setup instructions
└── tests/                    # Shared unit and integration tests
    ├── unit/                 # Unit tests for backend and NLP modules
    ├── integration/          # End-to-end pipeline and API tests
    └── README.md             # Testing guide
```

---

## 6. Standard Complaint Categories

The system strictly adheres to 6 standard category IDs across all modules:
1. `water_supply` — Water shortage, pipeline leaks, contaminated water.
2. `road_damage` — Potholes, damaged pavement, hazardous road conditions.
3. `garbage` — Overflowing bins, uncollected refuse, illegal dumping.
4. `drainage` — Blocked gutters, sewage overflow, storm drain clogs.
5. `streetlight` — Non-functional streetlights, broken fixtures, electrical hazards.
6. `other` — Miscellaneous grievances or items requiring manual categorization.

---

## 7. Next Steps

1. **Environment Setup**: Both members set up Python virtual environments (`.venv`).
2. **Dataset Acquisition (Member 1)**: Curate sample code-mixed complaints across the 6 categories (refer to `dataset/README.md`).
3. **Database Schema & CRUD (Member 2)**: Create SQLite models for complaints, departments, and citizen records in `backend/`.
4. **Baseline NLP Classifier (Member 1)**: Implement a baseline classifier meeting the response schema defined in `docs/api_contract.md`.
5. **Frontend Scaffold (Member 2)**: Initialize React (Vite) interface for complaint filing and triage.
