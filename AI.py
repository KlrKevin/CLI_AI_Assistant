import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

# list to keep the message history
messages = []

while True:
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
