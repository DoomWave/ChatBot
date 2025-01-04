import openai
openai.api_key = "https://api.openai.com/v1/chat/completions"
import tkinter

def chatBot ():
    print("Hello there!")

    while True: 
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Chatbot: See ya!")
            break
        elif "Hello" in user_input:
            print("Chatbot: Hi! How can I help you?")
