from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Portfolio data
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

# ✅ Home route (fixes "Not Found")
@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Portfolio API is running"
    })

# ✅ Portfolio API route
@app.route("/api/portfolio")
def get_portfolio():
    return jsonify(portfolio)


# Run locally
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
