from fastapi import FastAPI

app = FastAPI(
    title="AI Career Agent",
    description="AI-powered job matching and career optimization platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "AI Career Agent",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}