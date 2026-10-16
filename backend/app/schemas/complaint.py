"""API Schemas for Complaint Intake, Routing, and Listing."""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from nlp_engine.constants import ComplaintCategory
from nlp_engine.schemas import NLPAnalysisResponse


class ComplaintCreate(BaseModel):
    """Payload submitted by a citizen."""
    citizen_name: str = Field(..., min_length=2, max_length=100)
    citizen_phone: str = Field(..., min_length=10, max_length=15)
    ward_or_area: str = Field(..., min_length=2, max_length=100)
    address: str = Field(..., min_length=5, max_length=255)
    raw_complaint_text: str = Field(..., min_length=5)


class ComplaintStatusUpdate(BaseModel):
    """Payload submitted by municipal officer to update complaint status."""
    status: str = Field(..., pattern="^(received|in_progress|resolved|escalated)$")
    assigned_department: Optional[str] = None
    admin_notes: Optional[str] = None


class ComplaintSummaryItem(BaseModel):
    """Summary item displayed in municipal officer dashboard list."""
    complaint_id: str
    created_at: datetime
    citizen_name: str
    ward_or_area: str
    category: ComplaintCategory
    language: str
    summary: str
    status: str
    requires_human_review: bool


class ComplaintDetailResponse(BaseModel):
    """Complete complaint record returned upon submission or detail lookup."""
    complaint_id: str
    status: str
    created_at: datetime
    raw_complaint_text: str
    nlp_analysis: NLPAnalysisResponse
    assigned_department: str
    priority: str
