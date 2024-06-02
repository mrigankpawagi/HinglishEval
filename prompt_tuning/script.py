from openai import OpenAI
import os
import http.client
import json
import re
from dotenv import load_dotenv
from paraphraser import paraphrase
from breakdown import breakdown
from cross_lingual import cross_lingual


with open("../HumanEval.json") as f:
    data = json.load(f)

for problem in data:
    task_id = problem["task_id"].split("/")[-1]
    prompt = problem["prompt"]
    docstring = (re.findall(r'"""(.*?)"""', prompt, re.DOTALL) + re.findall(r"'''(.*?)'''", prompt, re.DOTALL))[0]

    try:
        res1 = paraphrase(docstring)
        res2 = breakdown(docstring)
        res3 = cross_lingual(docstring)
    except Exception:
        continue

    with open(f"drafts_1/{task_id}", "w", encoding="utf-8") as f1:
        f1.write(f'"""{docstring}"""\n\n"""\n{res1}\n"""')
    
    with open(f"drafts_2/{task_id}", "w", encoding="utf-8") as f2:
        f2.write(f'"""{docstring}"""\n\n"""\n{res2}\n"""')

    with open(f"drafts_3/{task_id}", "w", encoding="utf-8") as f3:
        f3.write(f'"""{docstring}"""\n\n"""\n{res3}\n"""')
