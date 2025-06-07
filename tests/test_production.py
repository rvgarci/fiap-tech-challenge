from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_production():
    response = client.get("/embrapa/producao?year=2000")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
