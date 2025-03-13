import pytest
from app import detect_fraud  # Import from your main app

def test_embedding_generation():
    fraud_status, _ = detect_fraud("Payment for groceries at Walmart")
    assert isinstance(fraud_status, str)

def test_faiss_similarity_search():
    fraud_status, similar_transactions = detect_fraud("Online purchase at Amazon")
    assert isinstance(similar_transactions, str)

def test_fraud_detection_accuracy():
    fraud_status, _ = detect_fraud("Suspicious international wire transfer $10,000")
    assert fraud_status in ["🚨 Fraudulent", "✅ Normal"]

def test_response_time():
    import time
    start = time.time()
    detect_fraud("Test transaction")
    end = time.time()
    assert (end - start) < 0.01  # Ensure response time < 10ms
