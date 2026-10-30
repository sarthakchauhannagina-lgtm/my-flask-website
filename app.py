# Step 1: Imports aur Flask App initialize karna
from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

# Step 2: Home route set karna
@app.route("/")
def home():
    return render_template("index.html")

# Step 3: Chat route aur Gemini API integration
@app.route("/chat", methods=["POST"])
def chat():
    try:
        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            return jsonify({
                "error": "Gemini API key set nahi hai."
            }), 500

        data = request.get_json(silent=True) or {}
        message = data.get("message", "").strip()

        if not message:
            return jsonify({
                "error": "Please enter a message."
            }), 400

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=message
        )

        return jsonify({
            "reply": response.text or "AI se jawab nahi mila."
        })

    except Exception:
        app.logger.exception("AI request failed")
        return jsonify({
            "error": "AI se connect nahi ho paya. Settings check karo."
        }), 500

# Step 4: App ko run karna
if __name__ == "__main__":
    app.run(debug=True)
    