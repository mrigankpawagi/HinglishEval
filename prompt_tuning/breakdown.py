from openai import OpenAI
import os
import http.client
import json
import re
from dotenv import load_dotenv

load_dotenv()

def docstring_translator(docstr):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a translator fluent in both Hindi and English. Today, you will breakdown prompts into subprompts. Given a prompt in English, you will break it into subprompts in Hinglish. Separate the subprompts by a semicolon ';' Note that all text must be in the Roman script, like in the example."
            },
            {
                "role": "user",
                "content": "Given a positive integer n, return the product of the odd digits.\n    Return 0 if all digits are even.\n    For example:\n    digits(1)  == 1\n    digits(4)  == 0\n    digits(235) == 15\n"
            },
            {
                "role": "assistant",
                "content": "Diye gaye positive integer n; n ke odd digits ka product return karo.;\n    Agar saare digits even ho to 0 return karo.;\n    Jaise ki:\n     digits(1)  == 1\n    digits(4)  == 0\n    digits(235) == 15\n"
            },
            {
                "role": "user",
                "content": docstr
            }
        ],
        temperature=0,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content
