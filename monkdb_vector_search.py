import psycopg2
from sentence_transformers import SentenceTransformer
import numpy as np
import json

# 1️⃣ Connect to MonkDB (PostgreSQL interface)
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="monkdb",
    user="misti",       # or "admin" if biswa user not created yet
    password="misti"   # or "admin" if using default credentials
)
cur = conn.cursor()
print("✅ Connected to MonkDB")

# 2️⃣ Create table for text and embeddings
cur.execute("""
CREATE TABLE IF NOT EXISTS ai_knowledge_base (
    id INTEGER PRIMARY KEY,
    title TEXT,
    content TEXT,
    embedding OBJECT
);
""")
conn.commit()
print("📦 Table created successfully.")

# 3️⃣ Load embedding model
print("⏳ Loading embedding model ...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("🤖 Model loaded.")

# 4️⃣ Insert sample data
docs = [
    ("AI Basics", "Artificial Intelligence allows computers to simulate human intelligence."),
    ("Machine Learning", "Machine learning helps systems learn automatically from data and experience."),
    ("Vector Databases", "Vector databases store embeddings to enable semantic similarity search."),
]

for idx, (title, content) in enumerate(docs, start=1):
    emb = model.encode(content).tolist()
    cur.execute(
        "INSERT INTO ai_knowledge_base (id, title, content, embedding) VALUES (%s, %s, %s, %s);",
        (idx, title, content, json.dumps(emb))
    )

conn.commit()
print("🧠 Sample data inserted.\n")

# 5️⃣ Query: find most similar documents
query = "How do computers learn from examples?"
qvec = model.encode(query).tolist()

cur.execute("SELECT title, content, embedding FROM ai_knowledge_base;")
rows = cur.fetchall()

# Cosine similarity
def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

results = []
for title, content, emb_str in rows:
    emb = json.loads(emb_str)
    sim = cosine_similarity(qvec, emb)
    results.append((title, content, sim))

# Sort by similarity
results.sort(key=lambda x: x[2], reverse=True)

# Display top results
print("🔍 Semantic Search Results:\n")
for title, content, sim in results[:3]:
    print(f"→ {title} | similarity = {sim:.4f}\n{content}\n")

cur.close()
conn.close()
print("✅ Done.")
