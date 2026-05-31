from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS (important for frontend connection)
CORS(app)

# ---------------- PORTFOLIO DATA ----------------
portfolio = {
    "skills": [
        "Graphic Design",
        "UI/UX",
        "Illustration",
        "Brand Identity",
        "Photography"
    ],
    "projects": [
        {
            "name": "Startup Branding",
            "description": "Developed a full brand identity for a tech startup."
        },
        {
            "name": "Mobile App UI",
            "description": "Designed user-friendly interfaces for a health tracking app."
        },
        {
            "name": "Children’s Book",
            "description": "Created illustrations for a published children’s storybook."
        },
        {
            "name": "Travel Photography",
            "description": "Curated a portfolio of lifestyle and travel photography."
        }
    ],
    "contact": {
        "email": "meshakimakala54@gmail.com",
        "phone": "0757447399"
    }
}

# ---------------- ROOT ROUTE ----------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "Portfolio API is running 🚀"
    })

# ---------------- GET PORTFOLIO ----------------
@app.route("/api/portfolio", methods=["GET"])
def get_portfolio():
    return jsonify(portfolio), 200

# ---------------- CONTACT MESSAGE API (FIXED) ----------------
@app.route("/api/message", methods=["POST"])
def send_message():
    try:
        data = request.get_json()

        # Validate input
        if not data:
            return jsonify({
                "status": "error",
                "message": "No data received"
            }), 400

        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        subject = data.get("subject", "").strip()
        message = data.get("message", "").strip()

        # Check required fields
        if not name or not email or not message:
            return jsonify({
                "status": "error",
                "message": "Name, email and message are required"
            }), 400

        # Print message (you can later store in DB or email it)
        print("\n📩 NEW CONTACT MESSAGE")
        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)
        print("====================================\n")

        return jsonify({
            "status": "success",
            "message": "Message received successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Server error",
            "error": str(e)
        }), 500


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
