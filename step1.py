from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Explain what an AI agent is in one sentence."},
    ],
)

print(response.choices[0].message.content)