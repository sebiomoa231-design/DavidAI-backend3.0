"""Render-compatible FastAPI entry point for David AI."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings import get_settings

settings = get_settings()

app = FastAPI(
    title="David AI",
    version=settings.APP_VERSION,
    debug=settings.ENV != "production",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "David AI backend is running", "version": settings.APP_VERSION}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "David AI"}


@app.get("/version")
def version() -> dict[str, str]:
    return {"version": settings.APP_VERSION}


@app.get("/api/status")
def status() -> dict[str, str]:
    return {"status": "online", "environment": settings.ENV}
