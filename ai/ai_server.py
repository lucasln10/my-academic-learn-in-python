from ollama import chat
from ollama import ChatResponse

def chatAi(text):
    response: ChatResponse = chat(model='qwen3.5:397b-cloud ', messages=[
    {
        'role': 'user',
        'content': text,
    },
    ])
    return response.message.content

print(chatAi("Ola"))