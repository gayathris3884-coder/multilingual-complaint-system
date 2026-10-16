"""Unit tests verifying the shared API contract and schema validation."""

import pytest
from pydantic import ValidationError
from nlp_engine.constants import ComplaintCategory, VALID_CATEGORY_IDS
from nlp_engine.schemas import NLPAnalysisResponse, DuplicateMatch


def test_complaint_category_ids():
    """Verify that the 6 exact complaint category IDs are defined and valid."""
    expected_categories = {
        "water_supply",
        "road_damage",
        "garbage",
        "drainage",
        "streetlight",
        "other",
    }
    actual_categories = {cat.value for cat in ComplaintCategory}
    assert actual_categories == expected_categories
    assert set(VALID_CATEGORY_IDS) == expected_categories


def test_valid_nlp_analysis_response():
    """Verify that a compliant NLP response succeeds schema validation."""
    data = {
        "language": "hi-Latn",
        "category": "drainage",
        "category_confidence": 0.88,
        "summary": "Report of gutter overflowing and waterlogging on main road.",
        "possible_duplicates": [
            {
                "complaint_id": "CMP-2026-1042",
                "similarity_score": 0.89,
                "snippet": "Main road gutter overflow issue near bus stand",
            }
        ],
        "requires_human_review": False,
    }
    response = NLPAnalysisResponse(**data)
    assert response.language == "hi-Latn"
    assert response.category == ComplaintCategory.DRAINAGE
    assert response.category_confidence == 0.88
    assert response.summary == "Report of gutter overflowing and waterlogging on main road."
    assert len(response.possible_duplicates) == 1
    assert response.possible_duplicates[0].complaint_id == "CMP-2026-1042"
    assert response.requires_human_review is False


def test_nlp_response_optional_confidence():
    """Verify that category_confidence can be null/None when model does not support it."""
    data = {
        "language": "en",
        "category": "streetlight",
        "category_confidence": None,
        "summary": "Broken streetlight outside block B.",
        "possible_duplicates": [],
        "requires_human_review": True,
    }
    response = NLPAnalysisResponse(**data)
    assert response.category_confidence is None
    assert response.requires_human_review is True


def test_nlp_response_invalid_category_rejection():
    """Verify that an invalid category ID is rejected by schema validation."""
    data = {
        "language": "en",
        "category": "electricity_theft",  # Invalid category ID
        "category_confidence": 0.95,
        "summary": "Illegal wiring detected.",
        "possible_duplicates": [],
        "requires_human_review": False,
    }
    with pytest.raises(ValidationError):
        NLPAnalysisResponse(**data)


def test_nlp_response_missing_required_fields():
    """Verify that missing required contract fields fail validation."""
    data = {
        "language": "hi-Latn",
        # missing category
        "summary": "Pani nahi aa raha hai",
        "possible_duplicates": [],
        "requires_human_review": True,
    }
    with pytest.raises(ValidationError):
        NLPAnalysisResponse(**data)
