from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_processing_historical():
    response = client.get("/embrapa/processamento/viniferas/historico")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
