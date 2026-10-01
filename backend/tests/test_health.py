from fastapi.testclient import TestClient

from project_ledger_api.main import app  # type: ignore[import-not-found]

client = TestClient(app)


def test_health_check_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
