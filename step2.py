from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

message = []

# response = client.chat.completions.create(
#     model="llama3.2",
#     messages=[
#         {"role": "user", "content": "Explain what an AI agent is in one sentence."},
#     ],
# )

# print(response.choices[0].message.content)

while True:
    user_input = input("User: ")
    if user_input.strip().lower() in ("exit", "quit"):
        break

    message.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama3.2",
        messages=message,
    )

    assistant_reply = response.choices[0].message.content
    message.append({"role": "assistant", "content": assistant_reply})
    print(f"Assistant: {assistant_reply}")
