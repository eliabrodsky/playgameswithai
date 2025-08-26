from fastapi.testclient import TestClient
from sqlmodel import SQLModel
from ..main import app
from ..database import engine, init_db

client = TestClient(app)

def setup_module(module):
    init_db()

def test_create_and_get_patient():
    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "dob": "1980-01-01",
        "last4_ssn": "1234"
    }
    resp = client.post("/patients", json=payload)
    assert resp.status_code == 200
    patient_id = resp.json()["id"]

    resp = client.get(f"/patients/{patient_id}")
    assert resp.status_code == 200
    assert resp.json()["first_name"] == "John"
