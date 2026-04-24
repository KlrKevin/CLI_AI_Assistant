import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

# list to keep the message history
messages = []

modes = {
    "1": "You are a helpful general assistant.",
    "2": "You summarize text clearly and concisely.",
    "3": "You generate creative and practical ideas.",
    "4": "You are a coding assistant that explains code simply.",
}

while True:
    for key in modes:
        print(f"{key}. {modes[key]}")

    mode_choice = input("choose your mode (1-4) ")

    if mode_choice not in modes.keys():
        print("please enter a number between 1-4")
        continue

    messages.append({"role": "system", "content": modes[mode_choice]})

    user_input = input("You:")

    # functionality to exit the loop
    if user_input.lower() == "exit":
        break

    # addsthe message we send to the api to a list, the list contains dictionaries as the api uses dictionaries as the message
    messages.append({"role": "user", "content": user_input})
    # role = who is speaking content = what hes saying

    # we call the api
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

    # storing the apis response
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print("AI:", reply)
