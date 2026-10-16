# Dataset Directory & Annotation Guidelines

## Overview
This directory is reserved for genuine multilingual and code-mixed complaint data. Per project requirements, **no fake or synthetic datasets have been generated here**.

Data collection and annotation will be managed primarily by **Member 1** with input from **Member 2** for domain validation.

---

## Directory Structure
- `raw/`: Unprocessed complaint texts directly harvested from public civic grievance portals, open-source municipal archives, or survey submissions.
- `processed/`: Cleaned, validated, and annotated datasets partitioned into `train.csv`, `val.csv`, and `test.csv`.

---

## Target Annotation Schema

Each processed complaint record must adhere to the following CSV / JSON schema:

| Column Name | Type | Allowed Values / Description |
|---|---|---|
| `id` | string | Unique record identifier (e.g., `RAW_0001`) |
| `text` | string | Original complaint text as entered by the citizen |
| `language` | string | Primary language tag (e.g., `en`, `hi`, `hi-Latn`, `mr`, `ta`) |
| `category` | string | Must be one of: `water_supply`, `road_damage`, `garbage`, `drainage`, `streetlight`, `other` |
| `summary` | string | Canonical human-verified summary in English |
| `is_code_mixed` | boolean | `true` if utterance mixes multiple languages (e.g., Hindi + English in Roman script) |

---

## Category Definitions for Annotators

1. `water_supply`:
   - Issues with municipal water pipelines, irregular water timings, contaminated drinking water, low pressure, water tanker shortages.
2. `road_damage`:
   - Potholes, damaged asphalt, missing pavers, dangerous road cavities, unpaved patches causing accidents.
3. `garbage`:
   - Overflowing public dustbins, uncollected community waste, illegal roadside garbage dumping, foul odor from trash piles.
4. `drainage`:
   - Clogged gutters, overflowing sewage pipelines, open manholes, stagnation of monsoon drainage water.
5. `streetlight`:
   - Dead streetlights, flickering fixtures, broken lampposts, dark stretches, hanging electrical wires on poles.
6. `other`:
   - Civic complaints falling outside the above five categories (e.g., stray animals, park maintenance, illegal banners).

---

## Ethical Guidelines
- **PII Scrubbing**: Remove personal names, specific phone numbers, and exact residential flat numbers from text before moving records to `processed/`.
- **Authenticity**: Preserve original misspellings, colloquial expressions, and transliteration variations (e.g., *'paani'*, *'pani'*, *'khadde'*, *'kachra'*), as these are essential for robust real-world NLP model training.
