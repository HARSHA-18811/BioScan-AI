from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .config import settings
from .database.database import init_db
from .routes import health, classes, predict, history, metrics, report

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize SQLite schema
    init_db()
    print("[BioScan AI] SQLite database initialized.")
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Educational & Research AI System for Biological Foliar Image Analysis",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routes
app.include_router(health.router)
app.include_router(classes.router)
app.include_router(predict.router)
app.include_router(history.router)
app.include_router(metrics.router)
app.include_router(report.router)

@app.get("/")
def root():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "operational",
        "docs_url": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
