# Nova — Rule-Based AI Chatbot 🤖

## DecodeLabs Artificial Intelligence — Project 1

### Project Goal
The goal of this project is to create a simple **rule-based AI chatbot** that responds to predefined user inputs.

This implementation follows the project requirements:
- Handles greetings.
- Handles exit commands.
- Uses `if-elif-else` decision logic.
- Runs in a continuous loop.
- Demonstrates basic AI decision-making and control flow.

## Features

Nova can:
- Respond to greetings such as `hi`, `hello`, and `hey`.
- Answer `how are you`.
- Tell its name.
- Explain what it can do.
- Show the current date.
- Show the current time.
- Display a help menu.
- Respond to thanks.
- Exit cleanly using `bye`, `exit`, or `quit`.
- Handle empty input and unknown input without crashing.
- Handle `Ctrl+C` / end-of-input gracefully.

## Requirements

- Python 3.x
- No external Python packages are required.

## Project Structure

```text
AI_Chatbot_Project/
├── chatbot.py
└── README.md
```

## How to Run

Open a terminal in the project folder and run:

```bash
python chatbot.py
```

If your system uses `python3`, run:

```bash
python3 chatbot.py
```

## Example Run

```text
====================================================
              NOVA - AI CHATBOT 🤖
====================================================
Rule-Based AI | DecodeLabs Project 1
Type 'help' for commands or 'bye' to exit.

You: hello
Nova: Hello! I am Nova. How can I help you?

You: what is your name
Nova: My name is Nova. I am a Rule-Based AI Chatbot.

You: what can you do
Nova: I can answer predefined questions, show the date/time, and handle basic conversation.

You: time
Nova: The current time is 01:30:20 PM.

You: bye
Nova: Goodbye! Thanks for chatting with me.
```

## How It Works

1. The program starts the chatbot.
2. A `while` loop continuously accepts user input.
3. The input is converted to lowercase so that `Hello`, `HELLO`, and `hello` can be handled consistently.
4. `if`, `elif`, and `else` rules compare the input with predefined patterns.
5. A matching response is displayed.
6. The loop continues until the user enters an exit command.

## Main Concepts Demonstrated

- Input and output
- Variables
- Functions
- `if-elif-else` statements
- `while` loop
- String processing
- Exception handling
- Basic rule-based AI
- Decision-making logic

## Why This Is Rule-Based AI

Nova does not learn from data. It follows explicit rules written by the programmer. For example:

```python
if text in {"hi", "hello", "hey"}:
    return "Hello!"
```

This is the core idea of a rule-based chatbot: **input → predefined rule → response**.

## Future Improvements

Possible extensions include:
- Add more rules and conversation topics.
- Store responses in dictionaries or files.
- Add a graphical user interface.
- Add conversation history.
- Add natural-language processing in a later project.

## Author

**Artificial Intelligence — Project 1**  
**Rule-Based AI Chatbot**
