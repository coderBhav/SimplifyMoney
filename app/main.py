from flask import Flask, request, jsonify
from db import init_db, add_user, add_purchase, get_last_user_id
import random

app = Flask(__name__)

init_db()

gold_facts = [
    "Gold has been used as money for over 5000 years.",
    "India is one of the largest consumers of gold in the world.",
    "Gold is considered a safe-haven investment during inflation.",
    "Central banks hold gold as part of their reserves."
]

gold_keywords = ["gold", "gold investment", "buy gold", "gold price", "investment in gold"]
yes_keywords = ["yes", "sure", "i want", "go ahead", "buy"]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    if any(word in user_input for word in gold_keywords):
        fact = random.choice(gold_facts)
        response = {
            "message": f"Here's a fact about gold: {fact}",
            "suggestion": "Do you want to purchase gold?"
        }
    elif any(word in user_input for word in yes_keywords):
        response = {
            "message": "Great! Please provide your name, email, and amount to proceed with the purchase.",
            "next_step": "/purchase"
        }
    else:
        response = {
            "message": "I specialize in gold investments. Ask me anything about gold!"
        }

    return jsonify(response)

@app.route("/purchase", methods=["POST"])
def purchase():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    amount = data.get("amount")

    add_user(name, email)

    user_id = get_last_user_id()

    add_purchase(user_id, amount)

    response = {
        "message": f"Gold purchase successful for {name} 💰",
        "amount": amount,
        "status": "SUCCESS"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)