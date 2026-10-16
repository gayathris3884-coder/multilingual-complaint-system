# API Contract Specification

## 1. Overview
This document specifies the shared interface contract between:
1. **Frontend Client (React + Vite)** and **Backend Service (FastAPI)**
2. **Backend Service** and **NLP Engine**

The goal is to maintain clear boundaries between team members and prevent schema mismatches during implementation.

---

## 2. Standard Complaint Categories

All services must use the following standard category IDs (exact string matching):

| Category ID | Description | Example Indicators |
|---|---|---|
| `water_supply` | Irregular supply, pipeline leaks, low pressure, contaminated water | "Pani nahi aa raha", "Water pipe burst" |
| `road_damage` | Potholes, broken tarmac, cave-ins, speed breaker issues | "Raste par khadde hain", "Broken road" |
| `garbage` | Uncollected waste, overflowing dumpsters, open dumping | "Kachra nahi uthaya", "Garbage overflow" |
| `drainage` | Clogged sewers, overflowing gutters, rainwater stagnation | "Gutter overflow ho raha hai", "Blocked drain" |
| `streetlight` | Non-functional lights, broken poles, exposed wiring | "Streetlight off hai", "Dark street, light broken" |
| `other` | Grievances outside predefined classes or unclassifiable | Miscellaneous complaints |

---

## 3. Common NLP Response Format

Whenever the NLP engine processes raw complaint text, it must return or map to this standard payload:

```json
{
  "language": "hi-Latn",
  "category": "drainage",
  "category_confidence": 0.88,
  "summary": "Report of gutter overflowing and waterlogging on main road for two days.",
  "possible_duplicates": [
    {
      "complaint_id": "CMP-2026-1042",
      "similarity_score": 0.89,
      "snippet": "Main road gutter overflow issue near bus stand"
    }
  ],
  "requires_human_review": false
}
```

### Schema Field Definitions

| Field | Type | Required | Description |
|---|---|---|---|
| `language` | `string` | Yes | Detected language/code-mixed tag (e.g., `en`, `hi`, `hi-Latn` / Hinglish, `mr-Latn`, `ta-Latn`, `unknown`). |
| `category` | `string` | Yes | One of the 6 exact category IDs (`water_supply`, `road_damage`, `garbage`, `drainage`, `streetlight`, `other`). |
| `category_confidence` | `float \| null` | Optional | Prediction confidence score between `0.0` and `1.0`. `null` if model does not produce calibrated probabilities. |
| `summary` | `string` | Yes | A concise canonical summary in English/standard language for administrative action. |
| `possible_duplicates` | `array[object]` | Yes | List of matched existing complaints flagged by semantic or spatial-textual similarity. Empty array `[]` if none found. |
| `requires_human_review` | `boolean` | Yes | `true` if confidence is low (e.g., `< 0.65`), category is `other`, code-switching ambiguity is high, or conflicting duplicate signals arise. |

---

## 4. Endpoints

### 4.1. Health Check
- **Endpoint**: `GET /api/v1/health`
- **Response** (`200 OK`):
```json
{
  "status": "healthy",
  "timestamp": "2026-10-16T21:00:00Z",
  "services": {
    "database": "connected",
    "nlp_engine": "ready"
  }
}
```

---

### 4.2. Analyze Complaint (NLP Direct Endpoint)
Used by the backend (or internal pipeline) to send raw complaint text to the NLP module.

- **Endpoint**: `POST /api/v1/nlp/analyze`
- **Request Body**:
```json
{
  "text": "Humare area me 2 din se gutter block hai aur pani road pe aa raha hai.",
  "location": "Ward 12, Shivaji Nagar",
  "include_duplicates": true
}
```
- **Response** (`200 OK`):
```json
{
  "language": "hi-Latn",
  "category": "drainage",
  "category_confidence": 0.91,
  "summary": "Blocked gutter causing wastewater overflow on road for 2 days in Ward 12.",
  "possible_duplicates": [],
  "requires_human_review": false
}
```

---

### 4.3. Submit Citizen Complaint
Main intake endpoint called by the frontend portal.

- **Endpoint**: `POST /api/v1/complaints`
- **Request Body**:
```json
{
  "citizen_name": "Rohan Sharma",
  "citizen_phone": "+919876543210",
  "ward_or_area": "Ward 12",
  "address": "Opposite Community Hall, MG Road",
  "raw_complaint_text": "Streetlight band hai 4 din se aur raat ko dark rehta hai."
}
```
- **Response** (`201 Created`):
```json
{
  "complaint_id": "CMP-2026-0001",
  "status": "received",
  "created_at": "2026-10-16T21:05:00Z",
  "raw_complaint_text": "Streetlight band hai 4 din se aur raat ko dark rehta hai.",
  "nlp_analysis": {
    "language": "hi-Latn",
    "category": "streetlight",
    "category_confidence": 0.94,
    "summary": "Streetlight non-functional for past 4 days causing low visibility at night.",
    "possible_duplicates": [],
    "requires_human_review": false
  },
  "assigned_department": "Electricity & Public Lighting",
  "priority": "medium"
}
```

---

### 4.4. List Complaints (Dashboard Query)
Used by the administrative dashboard for filtering, search, and triaging.

- **Endpoint**: `GET /api/v1/complaints`
- **Query Parameters**:
  - `category`: Filter by category ID (`water_supply`, `road_damage`, etc.)
  - `status`: `received` | `in_progress` | `resolved` | `escalated`
  - `requires_human_review`: `true` | `false`
  - `page`: default `1`
  - `limit`: default `20`
- **Response** (`200 OK`):
```json
{
  "total": 1,
  "page": 1,
  "limit": 20,
  "items": [
    {
      "complaint_id": "CMP-2026-0001",
      "created_at": "2026-10-16T21:05:00Z",
      "citizen_name": "Rohan Sharma",
      "ward_or_area": "Ward 12",
      "category": "streetlight",
      "language": "hi-Latn",
      "summary": "Streetlight non-functional for past 4 days causing low visibility at night.",
      "status": "received",
      "requires_human_review": false
    }
  ]
}
```

---

### 4.5. Department Routing & Status Update
Used by administrators to reassign or mark a grievance resolved.

- **Endpoint**: `PATCH /api/v1/complaints/{complaint_id}`
- **Request Body**:
```json
{
  "status": "in_progress",
  "assigned_department": "Electrical Maintenance Division",
  "admin_notes": "Technician dispatched"
}
```
- **Response** (`200 OK`):
```json
{
  "complaint_id": "CMP-2026-0001",
  "status": "in_progress",
  "assigned_department": "Electrical Maintenance Division",
  "updated_at": "2026-10-16T21:10:00Z"
}
```

---

## 5. Standard Error Format

All error responses must follow RFC 7807 compatible JSON structure:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid category ID provided.",
    "details": [
      {
        "field": "category",
        "issue": "Must be one of ['water_supply', 'road_damage', 'garbage', 'drainage', 'streetlight', 'other']"
      }
    ]
  }
}
```

### Standard HTTP Status Codes
- `200 OK`: Successful read or update.
- `201 Created`: Resource successfully created.
- `400 Bad Request`: Schema validation error or missing required inputs.
- `404 Not Found`: Complaint ID not found.
- `422 Unprocessable Entity`: Input format valid but semantic constraints violated.
- `500 Internal Server Error`: Unexpected runtime failure.
