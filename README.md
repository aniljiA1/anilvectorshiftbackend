🚀 VectorShift Pipeline Backend (FastAPI)

This repository contains the backend service for the VectorShift Frontend Technical Assessment.
It provides a simple FastAPI API that parses a pipeline graph, counts nodes and edges, and determines whether the pipeline forms a Directed Acyclic Graph (DAG).

🛠 Tech Stack

Python 3.10+

FastAPI

Uvicorn

Pydantic

CORS Middleware

📌 Features

Accepts pipeline data (nodes & edges) from frontend

Calculates:

Total number of nodes

Total number of edges

Whether the pipeline is a DAG

CORS enabled for frontend integration

Deployed on Render

📡 API Endpoints
POST /pipelines/parse

Parses the pipeline and returns graph metadata.

Request Body (JSON)
{
  "nodes": [
    { "id": "node-1" },
    { "id": "node-2" }
  ],
  "edges": [
    { "source": "node-1", "target": "node-2" }
  ]
}

Response
{
  "num_nodes": 2,
  "num_edges": 1,
  "is_dag": true
}

🔍 DAG Validation Logic

Builds a directed graph from edges

Uses DFS with recursion stack detection

Identifies cycles to determine DAG validity



2️⃣ Install dependencies
pip install fastapi uvicorn

3️⃣ Start the server
python -m uvicorn main:app --reload


Backend will run at:

http://127.0.0.1:8000

🌐 CORS Configuration

CORS is enabled to allow requests from the frontend:

allow_origins=["*"]


This can be restricted in production if needed.

☁️ Deployment (Render)

The backend is deployed using Render.

Live URL:
https://anilvectorshiftbackend.onrender.com
