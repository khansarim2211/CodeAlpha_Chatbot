# Basic Chatbot for CodeAlpha

def chatbot_response(user_input):
    """Return a response based on user input."""
    user_input = user_input.lower().strip()  # Normalize input
    responses = {
        "hello": "Hi! How can I assist you today?",
        "hi": "Hi! How can I assist you today?",
        "how are you": "I'm fine, thanks! How about you?",
        "what's your name": "I'm ChatBot, created for CodeAlpha!",
        "bye": "Goodbye! Have a great day!",
        "exit": "Goodbye! Have a great day!"
    }
    # Return matching response or default if no match
    return responses.get(user_input, "Sorry, I don't understand. Try 'hello', 'how are you', or 'bye'.")

def run_chatbot():
    """Main function to run the chatbot."""
    print("Welcome to CodeBot! Type 'bye' or 'exit' to quit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"CodeBot: {response}")
        if user_input.lower().strip() in ["bye", "exit"]:
            break

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()