# Backend Application (Member 2 Workspace)

## Responsibilities
Member 2 owns the development, deployment, and integration of the backend, database, and administrative routing:
1. **API Development**: Build and maintain FastAPI endpoints defined in `docs/api_contract.md`.
2. **Database Modeling**: Design SQLite schemas using SQLAlchemy for complaints, citizen records, department routing, and audit logs.
3. **Routing Engine**: Assign complaints to municipal departments based on category, ward, and urgency flags.
4. **Integration**: Route citizen submissions through the NLP engine and persist both raw and parsed outputs.
5. **Dashboard Queries**: Implement filtering, pagination, and status update endpoints for municipal staff.

## Running the Backend (Development)
```bash
# From workspace root
python -m venv .venv
# Activate virtual environment
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```
API Documentation will be available at `http://127.0.0.1:8000/docs`.
