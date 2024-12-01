import json

from huggingface_hub import login
login(token="<HUGGING_FACE_TOKEN>") 
# An access token from HUGGINGFACE is necessary to generate the code completions.

import os

from transformers import AutoModelForCausalLM, AutoTokenizer


def prompt_output(prompt, words):

    input_ids = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(**input_ids, max_new_tokens=words, do_sample=True)
    code_gen = tokenizer.decode(outputs[0])
    ind = code_gen.find("<eos>")
    if ind == -1:
        return code_gen[code_gen.index("<bos>") + 5 :]
    else:
        return code_gen[code_gen.index("<bos>") + 5 : ind]


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    path_humaneval = os.path.join(base_dir, "HinglishEval.json")

    gemma_codes_dir = os.path.join(base_dir, "gemma_7B_codes")
    os.makedirs(gemma_codes_dir, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b")
    model = AutoModelForCausalLM.from_pretrained("google/gemma-7b")

    with open(path_humaneval) as f:
        data = json.load(f)
        for pid in range(1, len(data)):  # Starting from 1 as per original code
            prompt = data[pid]["prompt"]
            with open(os.path.join(gemma_codes_dir, f"{str(pid).zfill(3)}.py"), "w") as file:
                file.write(prompt_output(prompt, 512))
                print(f"done for {pid}")

