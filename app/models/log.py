from sqlalchemy import Column, Integer, String, DateTime, Text, Index
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from app.database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    service_id = Column(String(100), nullable=False, index=True)  # e.g., 'auth-service', 'payment-service'
    level = Column(String(20), nullable=False)                    # 'INFO', 'WARN', 'ERROR', 'CRITICAL'
    status_code = Column(Integer, nullable=False)                # 200, 400, 500, etc.
    message = Column(Text, nullable=False)
    payload = Column(JSONB, nullable=True)                       # Unstructured metadata (e.g. user_id, ip_address)

    # Note: We are deliberately *not* adding complex composite indexes yet.
    # We want to experience the "Sequential Scan" performance penalty first!