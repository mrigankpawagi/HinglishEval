from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def docstring_translator(docstr):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": "You are a translator fluent in both Hindi and English. Today, you will convert docstrings of Python functions from English to Hinglish, which is a conversational form of Hindi in which we use English for technical words related to syntax or code, programming concepts, and mathematics. Note that all text must be in the Roman script, like in the example."
            },
            {
                "role": "user",
                "content": "Given a positive integer n, return the product of the odd digits.\\n    Return 0 if all digits are even.\\n    For example:\\n    digits(1)  == 1\\n    digits(4)  == 0\\n    digits(235) == 15\\n"
            },
            {
                "role": "assistant",
                "content": "Diye gaye positive integer n ke odd digits ka product return karo.\\n    Agar saare digits even ho to 0 return karo.\\n    Jaise ki:\\n     digits(1)  == 1\\n    digits(4)  == 0\\n    digits(235) == 15\\n"
            },
            {
                "role": "user",
                "content": docstr
            }
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    pass
