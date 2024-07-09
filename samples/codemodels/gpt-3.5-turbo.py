import json

import openai

openai.api_key = "<API-KEY>"


def gpt(docstr):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
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
    path_humaneval = (
        "/home/admin/AnirudhGupta/MultilingualBenchmarking_DBD/HinglishEval.json"
    )

    with open(path_humaneval) as f:
        data = json.load(f)
        for pid in [10, 32, 38, 50]:
            prompt = data[pid]["prompt"]
            with open(
                f"/home/admin/AnirudhGupta/MultilingualBenchmarking_DBD/gpt_3.5_turbo_codes/{str(pid).zfill(3)}.py",
                "w",
            ) as file:
                file.write(gpt(prompt))
                print(f"done for {pid}")
print("meow")

