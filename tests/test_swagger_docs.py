from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_swagger_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
