from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ ADD CORS HERE (RIGHT AFTER app = FastAPI())
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3004",
        "https://anilvectorshiftfrontend.vercel.app",
        "http://127.0.0.1:3004"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Ping": "Pong"}

@app.post("/pipelines/parse")
def parse_pipeline(pipeline: dict):
    nodes = pipeline.get("nodes", [])
    edges = pipeline.get("edges", [])

    return {
        "num_nodes": len(nodes),
        "num_edges": len(edges),
        "is_dag": True  # placeholder for now
    }
