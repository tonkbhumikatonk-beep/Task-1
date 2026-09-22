"""
Rule-Based AI Chatbot
DecodeLabs - Artificial Intelligence Project 1

A beginner-friendly console chatbot built with Python.
It uses explicit if/elif rules and a continuous loop.
"""

from datetime import datetime


BOT_NAME = "Nova"


def show_help():
    """Display available commands and topics."""
    print("\nNova: I can help with these topics:")
    print("  • greetings       - Say hello")
    print("  • how are you     - Check my status")
    print("  • your name       - Ask my name")
    print("  • time             - Show the current time")
    print("  • date             - Show today's date")
    print("  • help             - Show this menu")
    print("  • bye / exit / quit - End the chat\n")


def get_response(user_input):
    """Return a response based on predefined rules."""
    text = user_input.strip().lower()

    if not text:
        return "Please type something so I can respond."

    # Greetings
    if text in {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"}:
        return f"Hello! I am {BOT_NAME}. How can I help you?"

    # Well-being
    elif text in {"how are you", "how are you?", "how r u"}:
        return "I am doing great and ready to help!"

    # Identity
    elif text in {"your name", "what is your name", "what's your name"}:
        return f"My name is {BOT_NAME}. I am a Rule-Based AI Chatbot."

    # Capabilities
    elif text in {"what can you do", "what do you do", "help me"}:
        return "I can answer predefined questions, show the date/time, and handle basic conversation."

    # Help
    elif text in {"help", "commands", "menu"}:
        show_help()
        return None

    # Time
    elif text in {"time", "what is the time", "what time is it"}:
        return f"The current time is {datetime.now().strftime('%I:%M:%S %p')}."

    # Date
    elif text in {"date", "what is the date", "what date is it", "today"}:
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}."

    # Thanks
    elif text in {"thanks", "thank you", "thankyou"}:
        return "You're welcome!"

    # Exit
    elif text in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! Thanks for chatting with me."

    # Unknown input
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I can do."


def main():
    """Start and continuously run the chatbot."""
    print("=" * 52)
    print("              NOVA - AI CHATBOT 🤖")
    print("=" * 52)
    print("Rule-Based AI | DecodeLabs Project 1")
    print("Type 'help' for commands or 'bye' to exit.")

    while True:
        try:
            user_input = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{BOT_NAME}: Goodbye! Thanks for chatting with me.")
            break

        response = get_response(user_input)

        if response:
            print(f"{BOT_NAME}: {response}")

            if user_input.strip().lower() in {"bye", "goodbye", "exit", "quit"}:
                break


if __name__ == "__main__":
    main()
