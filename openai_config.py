from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
GITHUB_OPENAI_API_KEY = os.getenv("GITHUB_OPENAI_API_KEY")

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_OPENAI_API_KEY
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a concise technical assistant."},
        {"role": "user", "content": "how to learn software engineering and AI engineering faster than ever using ai tools"}
    ],
    temperature=0.2
)

print(response.choices[0].message.content)
