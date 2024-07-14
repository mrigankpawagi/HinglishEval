import json
import os

from openai import OpenAI


def phigen(docstr):
    # Create an OpenAI client with your deepinfra token and endpoint
    openai = OpenAI(
        api_key="api-key",
        base_url="https://api.deepinfra.com/v1/openai",
    )

    chat_completion = openai.chat.completions.create(
        model="microsoft/Phi-3-medium-4k-instruct",  ## MODEL NAME
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

    return chat_completion.choices[0].message.content


if __name__ == "__main__":

    path_humaneval = "/path/to/HinglishEval.json"

    try:
        os.mkdir("/path/to/unsanitized/Hinglish/phi-3-gen")
    except:
        pass

    with open(path_humaneval) as f:
        data = json.load(f)
        # for pid in [10, 32, 38, 50]: These pids are special. Take care of them seperately
        for pid in range(164):
            prompt = data[pid]["prompt"]
            with open(
                f"/path/to/unsanitized/Hinglish/phi-3-gen/{str(pid).zfill(3)}.py",
                "w",
            ) as file:
                file.write(phigen(prompt))
                print(f"done for {pid}")
        #    break

    path_humaneval = "/path/to/HumanEval.json"

    try:
        os.mkdir("/path/to/unsanitized/English/phi-3-gen")
    except:
        pass

    with open(path_humaneval) as f:
        data = json.load(f)
        # for pid in [10, 32, 38, 50]: These pids are special. Take care of them seperately
        for pid in range(164):
            prompt = data[pid]["prompt"]
            with open(
                f"/path/to/unsanitized/English/phi-3-gen/{str(pid).zfill(3)}.py",
                "w",
            ) as file:
                file.write(phigen(prompt))
                print(f"done for {pid}")
        #   break
