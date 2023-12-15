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
                "content": "You are a translator fluent in both Hindi and English. Today, you will convert docstrings of Python functions from English to Hinglish, which is a conversational form of Hindi in which we use English for technical words related to syntax, programming concepts, and mathematics. Note that all text must be in the Roman script, like in the examples."
            },
            {
                "role": "user",
                "content": "Make a list of ten Fibonacci numbers."
            },
            {
                "role": "assistant",
                "content": "Fibonacci numbers ki list banao jismei 7 numbers ho."
            },
            {
                "role": "user",
                "content": "Check if this word has length more than 3."
            },
            {
                "role": "assistant",
                "content": "Jaach karo ki kya iss shabd ki length 3 se upar hai ki nahi."
            },
            {
                "role": "user",
                "content": "Add two numbers a and b."
            },
            {
                "role": "assistant",
                "content": "Do numbers a aur b ko jodo."
            },
            {
                "role": "user",
                "content": "Check if given number is a perfect square."
            },
            {
                "role": "assistant",
                "content": "Jaach karo ki kya diya gaya number ek perfect square hai ki nahi."
            },
            {
                "role": "user",
                "content": "def function_name(arguments):"
            },
            {
                "role": "assistant",
                "content": "def function_name(arguments):"
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
