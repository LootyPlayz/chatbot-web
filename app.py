from flask import Flask, request, jsonify, render_template
from transformers import pipeline, set_seed

app = Flask(__name__)

# Load GPT-2 pipeline
generator = pipeline("text-generation", model="gpt2")
set_seed(42)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = generator(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
    return jsonify({"reply": response})

# Render deployment compatibility
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=False, host="0.0.0.0", port=port)
