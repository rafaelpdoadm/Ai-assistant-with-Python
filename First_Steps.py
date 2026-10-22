import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    messages= [
        {
            "role": "user",
            "content": "Explain what is an variable in python using two lines."
        }
    ]
)

for block in response.content:
    if block.type == "text":
        print(blocl.text)