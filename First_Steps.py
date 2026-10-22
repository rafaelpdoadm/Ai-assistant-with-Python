import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

MODEL = "claude-opus-5"

def ask(text):
    response = client.messages.create(
        model=MODEL,
        max_tokens=16000,
        messages= [
        {
            "role": "user",
            "content": text
        }
    ]
)

    result = ""
    for block in response.content:
        if block.type == "text":
            result = block.text

    return result


print(ask("O que é uma variável?"))