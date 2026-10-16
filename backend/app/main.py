"""FastAPI Application Entry Point."""

from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Multilingual and Code-Mixed NLP Framework for Public-Service Complaints",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for React frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/health", tags=["Health"])
def health_check():
    """Health check endpoint as defined in docs/api_contract.md."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "services": {
            "database": "configured",
            "nlp_engine": "ready"
        }
    }


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to the Multilingual Complaint Redressal API.",
        "documentation": "/docs",
        "health": "/api/v1/health"
    }
