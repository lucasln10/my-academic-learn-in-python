import os, httpx
from groq import Groq

client = Groq()

def inviteMessage(message: str) -> str:
    prompt = "você é um engenheiro de software muito experiente responda todas as perguntas da forna correta e sem enrolacao, quero respostas diretas com poucas linhas: " + message
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
        {
            "role": "user",
            "content": prompt
        }
        ],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="medium",
        stream=True,
        stop=None
    )

    response = ""

    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content

    return response
