from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Custom replies
custom_replies = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi! Kya haal hai?",
    "kya haal hai": "Sab badhiya! Tum sunao?",
    "how are you": "I'm doing great! Tum kaise ho?",
    "bye": "Bye! Jaldi milte hain!",
    "thank you": "You're welcome!",
    "kya tum insan ho": "Nahi, main ek AI hoon. Lekin dil se hoon ❤️",
    "tumhe kisne banaya": "I am made by LootyPlayz i.e. Gaurav.",
    "who made you": "I am made by LootyPlayz i.e. Gaurav.",
    "who make you": "I am made by LootyPlayz i.e. Gaurav.",
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip().lower()
    response = custom_replies.get(user_input, "Sorry, mujhe ye samajh nahi aaya. Aur kuch poochhna?")
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
