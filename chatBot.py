
def chatBot ():
    print("Hello there!")

    while True: 
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Chatbot: See ya!")
            break