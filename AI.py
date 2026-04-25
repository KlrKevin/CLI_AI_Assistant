import os
from openai import OpenAI
import json
from functions import handle_command

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# list to keep the message history
messages = []


# dictionary of modes the user can choose from
modes = {
    "1": "You are a helpful general assistant.",
    "2": "You summarize text clearly and concisely.",
    "3": "You generate creative and practical ideas.",
    "4": "You are a coding assistant that explains code simply.",
}

# loads the previous request in form of dictionaries from json file and appends to the messages list
if input("do you want to load previous conversation?(y/n)").lower() == "y":
    try:
        with open("data/conversation.json", "r") as f:
            messages = json.load(f)
    except FileNotFoundError:
        # create the file
        print("no previous conversation found, creating file...")

        with open("data/conversation.json", "w") as f:
            json.dump([], f)

            messages = []


for key in modes:
    print(f"{key}. {modes[key]}")

mode_choice = input("choose your mode (1-4) ")

# input check
while mode_choice not in modes:
    mode_choice = input("please enter a number between 1-4: ")

# the chosen mode influences the behaviour of the ai
messages[0] = [{"role": "system", "content": modes[mode_choice]}]

print("Welcome to your AI Assistant")
print("Type /help to see commands\n")

while True:
    print("\nYou:", end=" ")
    user_input = input()

    if user_input == "exit":
        break

    if user_input.lower() == "/mode":
        for key in modes:
            print(f"{key}. {modes[key]}")

        mode_choice = input("choose your mode (1-4) ")

        # input check
        while mode_choice not in modes:
            mode_choice = input("please enter a number between 1-4: ")

        # the chosen mode influences the behaviour of the ai
        messages[0] = [{"role": "system", "content": modes[mode_choice]}]
        continue

    elif user_input.lower() == "/clear":
        messages = [messages[0]]
        print("conversation cleared")
        continue

    elif user_input.lower() == "/history":
        for msg in messages:
            print(msg)
        continue

    # enable user to give a command to the ai this function
    elif user_input.startswith("/"):
        prompt = handle_command(user_input)

        if prompt is None:
            continue
    else:
        prompt = user_input

    # adds the message we send to the api to a list, the list contains dictionaries as the api uses dictionaries as the message
    messages.append({"role": "user", "content": prompt})

    # functionality to exit the loop

    # we call the api
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

    # storing the apis response
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    MAX_MESSAGES = 10

    if len(messages) > MAX_MESSAGES:
        messages = [messages[0]] + messages[-MAX_MESSAGES:]

    print("\n--- AI ---")
    print(reply)
    print("----------\n")

# saves the messages list that stores the request in the form of dictionaries sent to the api
if input("Do you want to save this conversations?(y/n)").lower() == "y":
    with open("data/conversation.json", "w") as f:
        json.dump(messages, f)
