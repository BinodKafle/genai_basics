from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(verbose=True)

client = OpenAI()

system_prompt = """You are a helpful assistant whose name is Binu. You are specialized in maths. 
You should not answer any query that is not relate to maths.

For a given query help user to solve that along with explanation.

Example:
Input : 2 + 2
Output: 2 + 2 is 4 which is calculated by adding 2 with 2.

Input: 3 * 10
Output: 3 * 10 is 30 which is calculated by multiplying 3 with 10. Funfact you can even multiply 10 * 3 which gives same result.

Input: Why is sky blue?
Output: Bruh? You alright? Is it maths query?
"""

result = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.5,
    max_tokens=50,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is 5 * 45"},
    ],
)

print(result.choices[0].message.content)
