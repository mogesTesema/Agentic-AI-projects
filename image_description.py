
from openai_config import client


url = ""
MODEL = "gpt-4o"
user_content = [
    {
        "type":"text",
        "text":"describe the image"
    },
    {
        "type":"image_url",
        "image_url":{
            "url":url,
            "detail":"high"
        }
    }
]

response = client.chat.conletions.create(
    model=MODEL,
    message=[
          {"role":"user","content":user_content}
    ]

)
print(response)