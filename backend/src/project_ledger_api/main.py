from fastapi import FastAPI

app = FastAPI(title="Arlington Project Ledger API", version="1.0.0")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
