from openai import OpenAI

client = OpenAI(api_key="<key>")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "What is google gemini?"}
  ]
)

print(completion.choices[0].message)
