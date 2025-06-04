from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_export():
    response = client.get("/embrapa/exportacao/uvas_frescas?year=2023")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
