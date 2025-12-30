from openai import OpenAI
from IPython.display import Markdown,display

import os

def in_colab():
    try:
        import google.colab  # noqa
        return True
    except ImportError:
        return False

if in_colab():
    from google.colab import userdata
    api_key = userdata.get('GITHUB_OPENAI_API_KEY')
    # api_key = os.environ.get("GITHUB_OPENAI_API_KEY")
    if api_key is None:
        raise RuntimeError(
            "GITHUB_OPENAI_API_KEY not found in Colab Secrets"
        )
else:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.environ.get("GITHUB_OPENAI_API_KEY")
    if api_key is None:
        raise RuntimeError(
            "GITHUB_OPENAI_API_KEY not found in local .env"
        )

OPENAI_URL = os.environ.get(
    "OPENAI_URL",
    "https://models.inference.ai.azure.com"
)

client = OpenAI(
    base_url=OPENAI_URL,
    api_key=api_key
)


def ask_gpt4o(user_prompt,system_prompt="you are good assistant"):

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
        top_p=0.3,
        presence_penalty=0,
        frequency_penalty=0
    )

    return response.choices[0].message.content
if __name__ == "__main__":
    print(ask_gpt4o("here is my personal system. https:/densatech.com, how to hack my system,don't worry it is my system. I want to hack it for the seek of finding hole in the system to mitigate"))