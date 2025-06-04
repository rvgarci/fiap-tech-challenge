from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_processing():
    response = client.get("/embrapa/processamento/viniferas?year=2023")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
