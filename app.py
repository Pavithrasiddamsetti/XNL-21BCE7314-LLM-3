import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the pretrained transformer model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS index and stored embeddings
index = faiss.read_index("faiss_index.bin")
stored_embeddings = np.load("transaction_embeddings.npy")

# Threshold for anomaly detection
ANOMALY_THRESHOLD = 0.3

def detect_fraud(transaction_text):
    """Processes a new transaction, computes embedding, and checks for fraud."""
    # Generate embedding
    transaction_embedding = model.encode([transaction_text])
    
    # Search in FAISS index
    D, I = index.search(transaction_embedding, 5)  # Get top 5 similar transactions
    avg_distance = np.mean(D)
    
    # Determine if the transaction is anomalous
    is_fraud = avg_distance > ANOMALY_THRESHOLD
    fraud_status = "🚨 Fraudulent" if is_fraud else "✅ Normal"
    
    return fraud_status, f"Top 5 Similar Transactions (Indexes): {I.tolist()}"
