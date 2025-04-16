from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(verbose=True)

client = OpenAI()

result = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}, # Zero Shot Prompting
    ],
)

print(result.choices[0].message.content)
