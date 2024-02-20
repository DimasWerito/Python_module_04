from openai import OpenAI
import os
from dotenv import dotenv_values


config = dotenv_values(".env")


api_key=config.get("OPENAI_API_KEY")
print(api_key)
client = OpenAI(api_key=api_key)
while True:
    user_input = input("Enter message: ")
    if user_input == "exit":
        break
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a technical assistant, \
         skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": user_input}
    ]
    )

    print(completion.choices[0].message)