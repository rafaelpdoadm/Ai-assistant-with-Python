import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

MODEL = "claude-opus-5"

SYSTEM_PROMPT= "Você é um tutor. Não entregue respostas prontas."

def ask(text):
    response = client.messages.create(
        model=MODEL,
        max_tokens=16000,
        system= SYSTEM_PROMPT,
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

### to put a personality and the response be diferent, i had to create a "rule" and give the instruction
### that is the easier way to put an personality and had an assistant with a certain way to respond

### rules = "Você é um tutor. Não entregue respostas prontas."
### print(ask(rules + "O que é uma variável?"))

### the way to use an especific personality is creating one new variable named "system" in the response configuration