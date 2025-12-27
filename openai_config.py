from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import Markdown,display

import os
load_dotenv()
GITHUB_OPENAI_API_KEY = os.getenv("GITHUB_OPENAI_API_KEY")
OPENAI_URL = os.getenv("OPENAI_URL","https://models.inference.ai.azure.com")

client = OpenAI(
    base_url=OPENAI_URL,
    api_key=GITHUB_OPENAI_API_KEY
)

def ask_gpt4o(user_prompt,system_prompt="you are good assistant"):

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
print(ask_gpt4o("how to send async request to any backend in python without any framework? give me some example code"))