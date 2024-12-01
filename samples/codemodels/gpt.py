import json
import os

import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def gpt(docstr):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Change to "gpt-4" if necessary. Check out more models at https://platform.openai.com/docs/models
        messages=[
            {
                "role": "system",
                "content": "You are an experienced Python programmer. Complete the Python functions from the given docstrings. Do NOT write anything except the function definition. Avoid print and input statements.\n",
            },
            {
                "role": "user",
                "content": f"Can you complete the following Python function? Retain the function header and docstring.\n\n```python\n{docstr}```",
            },
        ],
        temperature=0,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    path_humaneval = os.path.join(base_dir, "HinglishEval.json")

    with open(path_humaneval) as f:
        data = json.load(f)
        for pid in [10, 32, 38, 50]:
            prompt = data[pid]["prompt"]
            with open(
                os.path.join(base_dir, "gpt_3.5_turbo_codes", f"{str(pid).zfill(3)}.py"),
                "w",
            ) as file:
                file.write(gpt(prompt))
                print(f"done for {pid}")
