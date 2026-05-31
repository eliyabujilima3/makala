from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for frontend (VERY IMPORTANT)
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
        "email": "grace.ruge@portfolio.com",
        "phone": "+255-765-987-321",
        "linkedin": "https://linkedin.com/in/graceruge",
        "instagram": "https://instagram.com/graceruge",
        "behance": "https://behance.net/graceruge"
    },
    "qualifications": [
        "Bachelor of Arts in Graphic Design",
        "Certified UX/UI Specialist",
        "Adobe Creative Suite Expert",
        "5+ years professional experience in creative design"
    ]
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
    return jsonify(portfolio)

# ---------------- CONTACT FORM (FIX FOR YOUR FRONTEND ERROR) ----------------
@app.route("/api/message", methods=["POST"])
def send_message():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    name = data.get("name")
    email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")

    print("📩 New Message Received:")
    print(name, email, subject, message)

    return jsonify({
        "status": "success",
        "message": "Message received successfully"
    }), 200


# ---------------- RUN (RENDER SAFE) ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
