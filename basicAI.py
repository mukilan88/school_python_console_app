import random

def chatbot():
    print("Hi! I'm ChatBot, your friendly assistant.")
    print("Ask me anything or type 'bye' to exit.\n")

    responses = {
        "hello": ["Hi!", "Hello!", "Hey!"],
        "how are you": ["I'm good! How about you?", "Doing great, thank you!"],
        "your name": ["I'm ChatBot!", "You can call me ChatBot."],
        "age": ["I'm ageless!", "I don't have an age, just lines of code!"],
        "bye": ["Goodbye! See you!", "Take care! Bye!"]
    }

    while True:
        user_input = input("You: ").lower()

        if user_input in ["bye", "exit"]:
            print(random.choice(responses["bye"]))
            break

        # Find a response based on user input
        found_response = False
        for key in responses:
            if key in user_input:
                print("ChatBot:", random.choice(responses[key]))
                found_response = True
                break

        if not found_response:
            print("ChatBot: Sorry, I didn't understand that!")

chatbot()
