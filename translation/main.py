import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def docstring_translator(docstr):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You are a translator fluent in both Hindi and English. Today, you will convert docstrings of Python functions from English to Hinglish, which is a conversational form of Hindi in which we use English for technical words related to syntax, programming concepts, and mathematics. Note that all text must be in the Roman script, like in the examples."
      },
      {
        "role": "user",
        "content": "Make a list of ten fibonacci numbers "
      },
      {
        "role": "assistant",
        "content": "fibonacchi numbers ki list banao jismei 7 numbers ho"
      },
      {
        "role": "user",
        "content": "check if this word has length more than 3"
      },
      {
        "role": "assistant",
        "content": "jaach karo ki kya iss shabd ki length teen se upar hai ki nahi"
      },
      {
        "role": "user",
        "content": "add two numbers a and b"
      },
      {
        "role": "assistant",
        "content": "do numbers a aur b ko jodo"
      },
      {
        "role": "user",
        "content": "check if this number is a perfect square"
      },
      {
        "role": "assistant",
        "content": "jaach karo ki kya ye number ek perfect square hai ki nahi"
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
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response.choices[0].message.content
