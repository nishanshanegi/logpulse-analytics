from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from app.models.log import Log

def get_logs_paginated(db: Session, skip: int = 0, limit: int = 100, service_id: str = None):
    """Fetch logs with optional service filtering and pagination."""
    query = db.query(Log)
    if service_id:
        query = query.filter(Log.service_id == service_id)
    return query.order_by(desc(Log.timestamp)).offset(skip).limit(limit).all()

def get_error_summary_by_service(db: Session):
    """
    Get top services with the highest error counts (status_code >= 500)
    using Aggregations and Group By.
    """
    results = (
        db.query(
            Log.service_id,
            func.count(Log.id).label("error_count"),
            func.max(Log.timestamp).label("last_error_time")
        )
        .filter(Log.status_code >= 500)
        .group_by(Log.service_id)
        .order_by(desc("error_count"))
        .all()
    )
    
    return [
        {
            "service_id": row.service_id,
            "error_count": row.error_count,
            "last_error_time": row.last_error_time
        }
        for row in results
    ]