import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from datetime import datetime, timedelta
from faker import Faker
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.log import Log

# ... rest of your code ...
fake = Faker()

SERVICES = ["auth-service", "payment-service", "order-service", "notification-service", "api-gateway"]
LOG_LEVELS = ["INFO", "WARNING", "ERROR", "CRITICAL"]
STATUS_CODES = [200, 201, 400, 401, 403, 404, 500, 502, 503]

def generate_mock_logs(total_logs: int = 50_000, batch_size: int = 5000):
    db: Session = SessionLocal()
    print(f"🚀 Starting generation of {total_logs:,} mock logs...")
    
    start_time = datetime.utcnow() - timedelta(days=7)
    
    batch = []
    for i in range(1, total_logs + 1):
        # Random timestamp within the last 7 days
        random_timestamp = start_time + timedelta(seconds=random.randint(0, 604800))
        service = random.choice(SERVICES)
        level = random.choice(LOG_LEVELS)
        status = random.choice(STATUS_CODES)
        
        # Make errors correlate with 500/400 status codes for realism
        if status >= 500:
            level = "ERROR"
            msg = f"Internal server error while processing request in {service}"
        elif status >= 400:
            level = "WARNING"
            msg = f"Client request validation failed for {service}"
        else:
            level = "INFO"
            msg = f"Successfully processed request for {service}"

        log_entry = {
            "timestamp": random_timestamp,
            "service_id": service,
            "level": level,
            "status_code": status,
            "message": msg,
            "payload": {
                "ip_address": fake.ipv4(),
                "user_id": random.randint(1000, 99999),
                "endpoint": f"/api/v1/{service}/action",
                "latency_ms": random.randint(12, 1200)
            }
        }
        batch.append(log_entry)

        # Bulk insert when batch size is reached
        if len(batch) >= batch_size:
            db.bulk_insert_mappings(Log, batch)
            db.commit()
            batch = []
            print(f"Inserted {i:,} / {total_logs:,} logs...")

    # Insert any remaining logs
    if batch:
        db.bulk_insert_mappings(Log, batch)
        db.commit()

    db.close()
    print("✨ Successfully generated and inserted all mock logs!")

if __name__ == "__main__":
    generate_mock_logs(500,000) # Let's start with 50,000 to test speed