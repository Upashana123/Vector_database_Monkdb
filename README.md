Vector_database_Monkdb

This project demonstrates AI-powered semantic search using MonkDB as a unified, vector-capable database and Sentence Transformers for text embeddings.

It enables semantic similarity queries (like “how do computers learn?”) over text documents using vector embeddings and cosine similarity — entirely within MonkDB + Python.

🚀 Features

🧩 MonkDB integration via PostgreSQL-compatible API

🤖 AI embeddings using SentenceTransformer (all-MiniLM-L6-v2)

🔍 Semantic search powered by cosine similarity

💾 JSON-based vector storage

🐳 Easy setup with Docker + Python

🧠 Fully reproducible environment via requirements.txt

🛠️ Setup Instructions
1️⃣ Prerequisites

Make sure you have:

Docker installed and running

Python 3.10+ installed

(Optional but recommended) a virtual environment

2️⃣ Setup MonkDB

Pull and run the official MonkDB image (tested with dev150900/docker-dev-monk:v1):

# Create a Docker network for MonkDB
docker network create monkdb

# Run MonkDB container
docker run -d \
  --name monkdb01 \
  --net=monkdb \
  -p 4200:4200 -p 5432:5432 \
  -e MONKDB_USER=misti \
  -e MONKDB_PASSWORD=misti \
  dev150900/docker-dev-monk:v1


✅ MonkDB will now be available on:

SQL Port: 5432

Web API (if enabled): 4200

Check if it’s running:

docker ps


You should see something like:

CONTAINER ID   IMAGE                           PORTS
xxxxxx         dev150900/docker-dev-monk:v1    0.0.0.0:5432->5432/tcp, 0.0.0.0:4200->4200/tcp

3️⃣ Clone This Repository
git clone https://github.com/misti/monkdb_vector.git
cd monkdb_vector


If you want to host it under your own GitHub account, run:

git remote remove origin
git remote add origin https://github.com/<your_username>/<new_repo_name>.git
git push -u origin main

4️⃣ Create and Activate Virtual Environment
python3 -m venv monkdbenv
source monkdbenv/bin/activate


Then install dependencies:

pip install -r requirements.txt

5️⃣ Run the Project

Make sure MonkDB is running, then execute:

python monkdb_vector_search.py


✅ Expected Output:

✅ Connected to MonkDB
📦 Table recreated successfully.
🤖 Model loaded.
🔍 Semantic Search Results:



 Vector Databases
   Similarity: 0.6670
   Vector databases store embeddings to enable semantic similarity search.

✅ Done.

6️⃣ Project Structure
monkdb_vector/
│
├── monkdb_vector_search.py     # Main semantic search script
├── requirements.txt            # Dependencies for easy install
├── README.md                   # This file
└── .gitignore                  # Excludes env/cache files

💡 Notes

If MonkDB throws “data type not found” errors, ensure your container version is dev150900/docker-dev-monk:v1.

Embeddings are stored as JSON strings (not MonkDB vector type).

On first run, SentenceTransformer will download its model (~90 MB).

🧠 Credits

Project Author: Upashana Chatterjee

Database: MonkDB 2025.3.1
Embedding Model: all-MiniLM-L6-v2 (Sentence Transformers)

🧾 License

Released under the MIT License — free for personal, educational, and research use.
