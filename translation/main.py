import json
import os
import re

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def docstring_translator(docstr):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a translator fluent in both Hindi and English. Today, you will convert docstrings of Python functions from English to Hinglish, which is a conversational form of Hindi in which we use English for technical words related to syntax or code, programming concepts, and mathematics. Note that all text must be in the Roman script, like in the example."
            },
            {
                "role": "user",
                "content": "Given a positive integer n, return the product of the odd digits.\n    Return 0 if all digits are even.\n    For example:\n    digits(1)  == 1\n    digits(4)  == 0\n    digits(235) == 15\n"
            },
            {
                "role": "assistant",
                "content": "Diye gaye positive integer n ke odd digits ka product return karo.\n    Agar saare digits even ho to 0 return karo.\n    Jaise ki:\n     digits(1)  == 1\n    digits(4)  == 0\n    digits(235) == 15\n"
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


if __name__ == "__main__":

    base_dir = os.path.dirname(__file__)
    path_humaneval = os.path.join(base_dir, "HumanEval.jsonl")

    if path_humaneval is None:
        print("Please download the HumanEval.jsonl file as mentioned in README.md.")
        exit(1)

    with open(path_humaneval) as f:
        data = [json.loads(line) for line in f]

    for problem in data:
        task_id = problem["task_id"].split("/")[-1]
        prompt = problem["prompt"]
        docstring = (re.findall(r'"""(.*?)"""', prompt, re.DOTALL) + re.findall(r"'''(.*?)'''", prompt, re.DOTALL))[0]

        try:
            res = docstring_translator(docstring)
        except Exception:
            continue

        with open(f"drafts/{task_id}", "w", encoding="utf-8") as f:
            f.write(f'"""{docstring}"""\n\n"""\n{res}\n"""')
