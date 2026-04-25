def handle_command(user_input):

    parts = user_input.split(" ", 1)

    command = parts[0]
    content = parts[1] if len(parts) > 1 else ""

    if command == "/summarize":
        prompt = "Summarize this text clearly:\n" + content
        return prompt

    elif command == "/ideas":
        prompt = "Generate 5 creative ideas for:\n" + content
        return prompt

    elif command == "/code":
        prompt = "Explain this code simply:\n" + content
        return prompt

    elif command == "/help":
        print("""
                Available commands:
                /summarize <text>
                /ideas <topic>
                /code <code>
                /mode
                /clear
                /history
                exit
                """)
        return None

    else:
        return None
