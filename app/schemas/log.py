from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class LogResponse(BaseModel):
    id: int
    timestamp: datetime
    service_id: str
    level: str
    status_code: int
    message: str
    payload: Optional[Dict[str, Any]] = None

    class Config:
        from_attributes = True

class ErrorAnalyticsResponse(BaseModel):
    service_id: str
    error_count: int
    last_error_time: datetime