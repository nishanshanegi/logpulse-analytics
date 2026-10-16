# 🚀 LogPulse / AuditTrail
> High-Volume Enterprise Log Analytics & Audit Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-informational)](https://www.docker.com/)

## 🧠 The Project
LogPulse is a backend engineering project designed to simulate a high-throughput enterprise logging infrastructure. It ingests millions of system logs, security audit events, and API traces into PostgreSQL, exposing a lightning-fast analytics API. 

The primary goal of this project is to master **database query optimization, bulk data ingestion, and advanced indexing strategies** under high-load conditions.

---

## 🛠️ Core Engineering Features & Optimizations

- **High-Volume Ingestion:** Bypasses slow row-by-row ORM inserts using optimized bulk-writing techniques (Postgres `COPY` / batch execution).
- **Advanced Indexing Strategy:** 
  - *B-Tree Indexes* for range-heavy timestamp queries.
  - *Composite Indexes* carefully ordered to maximize query planner efficiency.
  - *Partial Indexes* to minimize index footprint and speed up error logging (status codes $\ge$ 500).
  - *GIN Indexes* for high-speed unstructured JSONB payload querying.
- **Complex Analytics API:** Leverages Common Table Expressions (CTEs), Window Functions (`ROW_NUMBER()`, `LAG()`), and advanced aggregations to serve dashboard data at scale.
- **Load Testing Suite:** Utilizes custom async Python load scripts to flood the API with thousands of requests to benchmark and prove query performance gains.

---

## 📊 Performance Benchmarks (The "Why")

| Query Type | Without Optimization (Seq Scan) | With Optimization (Indexed / Tuned) | Speedup |
| :--- | :--- | :--- | :--- |
| **Filter by Service & Timestamp Range (5M rows)** | ~3,500ms | **~12ms** | **~290x Faster** |
| **Error Status Filter (Partial Index)** | ~1,800ms | **~8ms** | **~225x Faster** |
| **JSONB Payload Search (GIN Index)** | ~4,200ms | **~25ms** | **~168x Faster** |

*(Benchmarks run locally via `EXPLAIN ANALYZE` on a 5-million row mock dataset)*

---

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.10+

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/logpulse-analytics.git
   cd logpulse-analytics