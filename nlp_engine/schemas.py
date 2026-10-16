"""Data schemas for NLP Engine requests and responses adhering to docs/api_contract.md."""

from typing import List, Optional
from pydantic import BaseModel, Field
from nlp_engine.constants import ComplaintCategory


class DuplicateMatch(BaseModel):
    """Represents a potential duplicate complaint identified by semantic/spatial matching."""
    complaint_id: str = Field(..., description="ID of the matched existing complaint")
    similarity_score: float = Field(..., ge=0.0, le=1.0, description="Similarity score between 0.0 and 1.0")
    snippet: Optional[str] = Field(None, description="Excerpt or summary of the matched complaint")


class NLPAnalysisRequest(BaseModel):
    """Input payload for NLP analysis pipeline."""
    text: str = Field(..., min_length=1, description="Raw complaint text submitted by citizen")
    location: Optional[str] = Field(None, description="Ward or geographic location to aid deduplication")
    include_duplicates: bool = Field(True, description="Whether to perform duplicate detection query")


class NLPAnalysisResponse(BaseModel):
    """Standardized common NLP response format."""
    language: str = Field(..., description="Detected language/code-mixed tag (e.g., 'en', 'hi', 'hi-Latn')")
    category: ComplaintCategory = Field(..., description="One of the 6 exact complaint category IDs")
    category_confidence: Optional[float] = Field(
        None,
        ge=0.0,
        le=1.0,
        description="Confidence score for predicted category, when supported by the model"
    )
    summary: str = Field(..., description="Concise administrative summary in standard language")
    possible_duplicates: List[DuplicateMatch] = Field(
        default_factory=list,
        description="List of possible duplicate complaints"
    )
    requires_human_review: bool = Field(
        ...,
        description="Flag indicating if low confidence, ambiguity, or conflict warrants manual review"
    )
