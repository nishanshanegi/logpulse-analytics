from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.crud.log import get_logs_paginated, get_error_summary_by_service
from app.schemas.log import LogResponse, ErrorAnalyticsResponse

router = APIRouter(prefix="/logs", tags=["Logs Analytics"])

@router.get("/", response_model=List[LogResponse])
def read_logs(
    skip: int = 0, 
    limit: int = 50, 
    service_id: str = Query(None, description="Filter by microservice name"),
    db: Session = Depends(get_db)
):
    """Endpoint to fetch raw logs with pagination and optional service filter."""
    logs = get_logs_paginated(db, skip=skip, limit=limit, service_id=service_id)
    return logs

@router.get("/analytics/errors", response_model=List[ErrorAnalyticsResponse])
def get_error_analytics(db: Session = Depends(get_db)):
    """Analytics dashboard endpoint showing error breakdowns per microservice."""
    return get_error_summary_by_service(db)