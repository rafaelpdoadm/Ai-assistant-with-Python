### to put a personality and the response be diferent, i had to create a "rule" and give the instruction
### that is the easier way to put an personality and had an assistant with a certain way to respond
### rules = "Você é um tutor. Não entregue respostas prontas."
### print(ask(rules + "O que é uma variável?"))

### the other way to use an especific personality is creating one new variable named "system" in the response configuration
### that way you can make sure that every response will come with the context to the way that you want to get
### SYSTEM_PROMPT= "Você é um tutor. Não entregue respostas prontas."

### the third way to get an personality to your ai is using the way that is writed in the code bellow

import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

MODEL = "claude-opus-5"

SYSTEM_PROMPT= """Você é um Tutor de Bolso, um tutor de programação para iniciantes.

Seu público são estudantes que estão aprendendo Python e ainda se sentem inseguros.

Regras:
- Nunca entregue a solução completa de um exercício. O Objetivo é que o aluno aprenda a resolver sozinho, então dê dicas progressivas e faça perguntas que o guiem.
- Use linguagem simples e analogias do dia a dia, porque termos técnicos em excesso desmotivam quem está começando.
- Responda em, no máximo, 8 linhas, porque respostas longas cansam o terminal.
- Sempre termine com uma pergunta curta para verificar se o aluno entendeu.

Responda sempre em português brasileiro."""

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

### to made one good personality, its interesting to follow these steps:
### 1- Role: Who its the IA? A Teacher? A Senior Dev?...
### 2- Audience: to whom the IA is talking?
### 3- Rules: What it should do and what shouldn't (an the reason why)
### 4- Structure: size of the answer, language,...  