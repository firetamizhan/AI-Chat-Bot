import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thanks!', 'I am doing well, how about you?']),
    (r'what is your name', ['I am a chatbot.', 'My name is ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

def chat_with_bot():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download("punkt")
    chat_with_bot()

