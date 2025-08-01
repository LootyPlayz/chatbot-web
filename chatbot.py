from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create the chatbot
chatbot = ChatBot(
    'MyBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    read_only=True
)

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")  # You can also try "chatterbot.corpus.english.greetings"

# Start chatting
print("Chatbot is ready! Type something or 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Bye! Have a nice day!")
        break
    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
