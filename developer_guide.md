# Developer Guide

## 📂 Code Structure
- **`app.py`** → Main fraud detection logic.
- **`tests/`** → Unit tests for fraud detection.
- **`results/`** → Benchmark & analysis reports.
- **`scripts/`** → Deployment scripts.

## 🛠️ How It Works
1️⃣ **Embeddings are generated** using `sentence_transformers`.  
2️⃣ **FAISS performs similarity search** to detect anomalies.  
3️⃣ **Transactions flagged** based on similarity scores.  

## 📡 API Documentation
- **`detect_fraud(transaction: str) → (status, similar_transactions)`**  
  - **Input:** Transaction description (string).  
  - **Output:** Fraud status (`✅ Normal` or `🚨 Fraudulent`) and similar past transactions.  

## 🏗 System Requirements
- **Python 3.11+**
- **FAISS, sentence_transformers, pytest**
- **Flask (for API deployment)**
