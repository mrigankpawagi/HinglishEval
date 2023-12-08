# This code is for v1 of the openai package: pypi.org/project/openai
import openai

openai.api_key = "sk-YOUR-OPENAI-API-KEY"
def docstring_translator(docstr):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You are a translator which translates English docstrings of codes in hindi using English characters. It should NOT contain hindi character like दस,दी गई, संख्याओं , etc. but should have das, numbers, etc. Some English words like numbers, list, strings, fibonacci, etc. are allowed to put in translated text."
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
# print(docstring_translator("Make a list of ten prime numbers"))
# OUTPUT: dus prime numbers ki list banao
