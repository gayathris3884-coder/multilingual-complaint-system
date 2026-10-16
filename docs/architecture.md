# System Architecture

## 1. High-Level Architecture

```
                    ┌──────────────────────────────┐
                    │        Citizen Portal        │
                    │        (React / Vite)        │
                    └──────────────┬───────────────┘
                                   │ HTTP POST (Complaint)
                                   ▼
                    ┌──────────────────────────────┐
                    │      FastAPI Backend         │
                    │    (Validation & Auth)       │
                    └──────┬───────────────┬───────┘
                           │               │
         Internal Analysis │               │ Persist & Query
                           ▼               ▼
           ┌──────────────────────┐   ┌──────────────────────┐
           │      NLP Engine      │   │   SQLite Database    │
           │                      │   │                      │
           │ • Script Detector    │   │ • Complaints Table   │
           │ • Code-Mix Processor │   │ • Categories Table   │
           │ • Classifier         │   │ • Department Routing │
           │ • Deduplicator       │   │ • Audit Logs         │
           │ • Summarizer         │   └──────────────────────┘
           └──────────────────────┘              ▲
                                                 │
                                   ┌─────────────┴────────┐
                                   │  Admin Review Board  │
                                   │  (Municipal Portal)  │
                                   └──────────────────────┘
```

---

## 2. Component Breakdown

### 2.1. Citizen Portal (Frontend)
- Clean, accessible web interface for citizens to submit grievances in English or native/code-mixed scripts.
- Shows instant receipt acknowledgment and unique tracking ID (`CMP-YYYY-XXXX`).

### 2.2. Backend Gateway (FastAPI)
- Enforces payload validation against `docs/api_contract.md`.
- Connects intake requests with the NLP Engine.
- Manages transaction persistence into SQLite.
- Executes departmental dispatch routing.

### 2.3. NLP Engine
- **Step 1: Script & Language Identification**: Recognizes romanized vernacular (`hi-Latn`) vs pure native script vs English.
- **Step 2: Normalization**: Handles informal spelling variants and removes noise.
- **Step 3: Classification**: Maps text into one of 6 exact category IDs (`water_supply`, `road_damage`, `garbage`, `drainage`, `streetlight`, `other`).
- **Step 4: Deduplication**: Vector search across open complaints in the vicinity.
- **Step 5: Summarization**: Canonical concise English summary for civic officers.
- **Step 6: Confidence Gate**: Flags `requires_human_review = True` if confidence < 0.65 or if category is `other`.

### 2.4. Municipal Officer Dashboard
- Enables civic authorities to view queued complaints, filter by category or ward, review low-confidence items, and update grievance status.
