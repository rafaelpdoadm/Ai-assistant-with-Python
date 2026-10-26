### following the last class, what can be do to have continuous talk with the AI?
### writing a "while" and a "break"

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

### the code bellow is the new part added

print("Bem-vindo(a) ao tutor de bolso!")
print("Digite 'sair' para finalizar a conversa.")

while True:
    text = input("Você: ").strip()

    if text.lower() == "sair":
        print("Bons estudos!")
        break
    if not text:
        continue

    print(ask(text))