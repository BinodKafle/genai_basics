from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = "Eiffel Tower is in Paris and is a famous landmark. It is one of the most recognizable structures in the world."

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

print("Vector Embeddings", response.data[0].embedding)  # Vector Embeddings: [-0.123456, 0.654321, ...]