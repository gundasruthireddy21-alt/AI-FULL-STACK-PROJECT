import ollama

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "What is Python?"
        }
    ]
)

print(response["message"]["content"])