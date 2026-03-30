import requests
from groq import Groq

#dentro dos colocar a chave da api
client = Groq()

def inviteMessage(message):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
        {
            "role": "user",
            "content": message
        }
        ],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="medium",
        stream=True,
        stop=None
    )

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")


def inputForMessage():
    print("Faca uma pergunta qualquer: ")
    message = input()
    print("\n")
    inviteMessage(message)

inputForMessage()