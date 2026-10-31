from flask import Flask, render_template
from google import genai
client = genai.Client()
app = Flask(__name__)

@app.route("/")
def home():
    response = client.models.generate_content (model="gemini-3.5-flash", contents="Hello")
    return response.text

if __name__ == "__main__":
    app.run(debug=True)

    
