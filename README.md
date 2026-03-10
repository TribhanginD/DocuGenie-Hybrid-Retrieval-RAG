---
title: DocuGenie
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---

# DocuGenie: Hybrid Retrieval & Reranking System (RAG)

DocuGenie is the central coordination hub of the **Unified AI Platform**. It leverages a production-grade Retrieval-Augmented Generation (RAG) engine to provide interactive document Q&A while delegating specialized governance and reliability tasks to dedicated microservices.

## 🏗️ Unified Platform Architecture

DocuGenie acts as the orchestrator in a "triangular" dependency model:
1. **DocuGenie (The Orchestrator)**: Manages RAG, user interaction, and service delegation.
2. **Real-Time ML Pipeline (Governance Service)**: Scans all ingested content for PII and compliance violations.
3. **Order Processing System (Reliability Engine)**: Ensures idempotent ingestion and handles background task persistence.
4. **DevOps Copilot / Incident Center**: Provides real-time telemetry and incident management for the entire stack.

## ✨ Features

- **Service Delegation** — Offloads compliance scanning and reliable ingestion to external specialized engines.
- **Hybrid Search** — BM25 + Qdrant vector search for precision recall.
- **Gemini-powered Reranking** — Listwise reranking for top-quality results.
- **Modern React UI** — Glassmorphic design with smooth animations.
- **Full Observability** — Exports metrics to Prometheus/Grafana for the AI SRE control plane.

## 🚀 Zero-Cost Deployment

To deploy the unified platform to Hugging Face Spaces:

### 1. Configure Environment
In your DocuGenie Space settings, add the following **Variables**:
- `ML_PIPELINE_URL`: URL of your deployed `real-time-ml-pipeline` Space.
- `ORDER_SYSTEM_URL`: URL of your deployed `order-processing-system` Space.

### 2. Provider API Keys
- `GOOGLE_API_KEY`: Required for Gemini LLM and Embeddings.
- `GROQ_API_KEY`: Optional fallback for Llama-3 models.

---

## 📊 Benchmarks

| Metric | Score |
|---|---|
| Mean Reciprocal Rank (MRR) | **1.0** |
| Precision@5 | **0.56** |
| Avg Retrieval Latency | **1.24s** |

## 🛠️ Tech Stack

React · Vite · TailwindCSS · FastAPI · Qdrant · Gemini · Groq · Prometheus

## 📄 License

MIT
