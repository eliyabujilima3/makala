from flask import Flask, jsonify
from flask_cors import CORS   # ✅ Import CORS

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS globally

# Manual portfolio details
portfolio = {
    "skills": [
        "Graphic Design",
        "UI/UX",
        "Illustration",
        "Brand Identity",
        "Photography"
    ],
    "projects": [
        {"name": "Startup Branding", "description": "Developed a full brand identity for a tech startup."},
        {"name": "Mobile App UI", "description": "Designed user-friendly interfaces for a health tracking app."},
        {"name": "Children’s Book", "description": "Created illustrations for a published children’s storybook."},
        {"name": "Travel Photography", "description": "Curated a portfolio of lifestyle and travel photography."}
    ],
    "contact": {
        "email": "grace.ruge@portfolio.com",   # ✅ Updated email
        "phone": "+255-765-987-321",           # ✅ Updated phone
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

# API route
@app.route("/api/portfolio")
def get_portfolio():
    return jsonify(portfolio)

if __name__ == "__main__":
    app.run(debug=True)
