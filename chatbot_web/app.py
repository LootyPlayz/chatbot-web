from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create Flask app
app = Flask(__name__)

# Create chatbot instance
chatbot = ChatBot('WebBot', read_only=True)

# Train the bot using built-in English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Route to serve the chat webpage
@app.route("/")
def home():
    return render_template("index.html")

# Route to get chatbot response via JavaScript
@app.route("/get")
def get_response():
    user_input = request.args.get("msg")  # Get user message from query string
    bot_response = chatbot.get_response(user_input)
    return jsonify(str(bot_response))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
