from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_commercial_historical():
    response = client.get("/embrapa/comercializacao/historico")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
