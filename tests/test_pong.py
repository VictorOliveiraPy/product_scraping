from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_check_return_message():
    response = client.get("/")

    assert response.json() == {"message": "Fullstack Challenge 20201026"}
