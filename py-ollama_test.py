from ollama import chat

# Specify the model you want to use
model_name = 'Cel'

# Infinite loop for chat interaction
while True:
    try:
        # Get user input
        user_input = input("You: ")
        
        # Exit the loop if the user types 'exit' or 'quit'
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat. Goodbye!")
            break

        # Send the user input to the chat model
        stream = chat(
            model=model_name,
            messages=[{'role': 'user', 'content': user_input}],
            stream=True,
        )

        # Print the response as it's streamed
        print("AI: ", end="", flush=True)
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
        print()  # Add a newline after the response

    except KeyboardInterrupt:
        print("\nExiting the chat. Goodbye!")
        break
    except Exception as e:
        print(f"An error occurred: {e}")

