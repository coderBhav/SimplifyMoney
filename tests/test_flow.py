# tests/test_flow.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_end_to_end():
    uid = "u_test"

    r1 = client.post("/chat", json={"user_id": uid, "user_query": "hi"})
    assert r1.status_code == 200

    r2 = client.post("/chat", json={"user_id": uid, "user_query": "I want to invest in gold"})
    assert r2.json()["intent"] == "gold_investment"
    assert r2.json()["next_action"] == "confirm_purchase"

    r3 = client.post("/chat", json={"user_id": uid, "user_query": "yes buy"})
    assert r3.json()["next_action"] == "ask_amount"

    r4 = client.post("/chat", json={"user_id": uid, "user_query": "1 gram"})
    assert r4.json()["next_action"] == "go_to_purchase"

    r5 = client.post("/purchase", json={"user_id": uid, "amount_grams": 1.0, "payment_method": "wallet"})
    assert r5.status_code == 200
    assert r5.json()["status"] == "success"

    r6 = client.get(f"/purchases/{uid}")
    assert r6.status_code == 200
    assert len(r6.json()) >= 1
