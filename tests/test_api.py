import requests

BASE_URL = "http://127.0.0.1:5000"

def test_two_step_workflow():
    print("Step 1: Ask about gold")
    chat_data = {"message": "Tell me about gold investment"}
    chat_resp = requests.post(f"{BASE_URL}/chat", json=chat_data)
    chat_json = chat_resp.json()
    print(chat_json)

    assert "message" in chat_json
    assert "suggestion" in chat_json

    print("\nStep 2: User says YES")
    chat_yes_data = {"message": "Yes, I want to buy"}
    chat_yes_resp = requests.post(f"{BASE_URL}/chat", json=chat_yes_data)
    chat_yes_json = chat_yes_resp.json()
    print(chat_yes_json)

    assert "message" in chat_yes_json
    assert chat_yes_json.get("next_step") == "/purchase"

    print("\nStep 3: Make purchase")
    purchase_data = {
        "name": "Bhawna Chaturvedi",
        "email": "bhawna@yahoo.com",
        "amount": 10
    }
    purchase_resp = requests.post(f"{BASE_URL}/purchase", json=purchase_data)
    purchase_json = purchase_resp.json()
    print(purchase_json)

    assert purchase_json.get("status") == "SUCCESS"
    assert purchase_json.get("amount") == 10
    assert "Gold purchase successful" in purchase_json.get("message")

    print("\nTwo-step workflow test completed successfully!")

if __name__ == "__main__":
    test_two_step_workflow()