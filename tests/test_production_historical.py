from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_production_historical():
    response = client.get("/embrapa/producao/historico")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
