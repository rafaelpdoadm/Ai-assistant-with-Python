## the following uptdate has the intention of giving memory to the AI
## with this, it should be easier to get a continuous talk with the memory of the past answers

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

def ask(text, history):
    history.append({"role": "user", "content": text})
    response = client.messages.create(
        model = MODEL,
        max_tokens = 16000,
        system = SYSTEM_PROMPT,
        messages = history
    ]
)

    result = ""
    for block in response.content:
        if block.type == "text":
            result = block.text

    history.append({"role":"assistant", "content": result})
    
    return result

print("Bem-vindo(a) ao tutor de bolso!")
print("Digite 'sair' para finalizar a conversa.")

## memory update code
history = []

while True:
    text = input("Você: ").strip()

    if text.lower() == "sair":
        print("Bons estudos!")
        break

    if text.lower() == "limpar":
        history = []
        print("Tutor: Conversa reiniciada. Do que vamos falar agora?")
        
    if not text:
        continue

    print(ask(text, history))