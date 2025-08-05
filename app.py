from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

chat = pipeline("text-generation", model="gpt2")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_route():
    user_input = request.json['message']
    if user_input.lower() in ["who made you", "who made u", "tumhe kisne banaya", "who make u"]:
        return jsonify({'reply': "I am made by LootyPlayz i.e. Gaurav"})

    response = chat(user_input, max_new_tokens=50, do_sample=True)[0]['generated_text']
    reply = response[len(user_input):].strip()
    return jsonify({'reply': reply})

if __name__ == '__main__':
    # Port default 5000 if not set
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
