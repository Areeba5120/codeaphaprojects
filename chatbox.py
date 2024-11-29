import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have downloaded the necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define chatbot patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I assist you with?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created to assist you. You can call me Chatbot!",]
    ],
    [
        r"how are you ?",
        ["I'm here to help you! How can I assist?", "I'm just a bot, but thanks for asking!"]
    ],
    [
        r"what can you do ?",
        ["I can answer questions and have simple conversations. What would you like to know?"]
    ],
    [
        r"how to learn python ?",
        ["There are many ways to learn Python! You can check out online tutorials, courses, and practice projects.",]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you soon!"]
    ],
]

# Set up a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the chatbot conversation
print("Chatbot: Hi there! Type something to start a conversation. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        response = chatbot.respond(user_input)
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase?")
