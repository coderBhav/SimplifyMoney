# Simplify Money AI Intern Assignment
This project implements a two-step gold investment workflow similar to Kuber.ai:

1. /chat API 
   Detects gold-related questions
   Returns a random fact about gold
   Suggests the user to purchase gold
2. /purchase API  
   Accepts user name, email, and gold amount
   Records user and purchase in SQLite database
   Returns a success message

---

## How to Run

1. Activate virtual environment:
   venv\Scripts\activate
2. Install dependencies:
pip install -r requirements.txt
3. Run the Flask server:
python app/main.py
4. Test the workflow using the test script:
python tests/test_api.py