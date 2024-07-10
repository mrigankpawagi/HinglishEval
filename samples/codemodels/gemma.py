import json

# from huggingface_hub import login
# login(token="<HUGGING_FACE_TOKEN>") # might be necessary
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

    path_humaneval = "/path/to/HinglishEval.json"

    try:
        os.mkdir("/path/to/gemma_7B_codes")
    except:
        pass

    tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b")
    model = AutoModelForCausalLM.from_pretrained("google/gemma-7b")

    with open(path_humaneval) as f:
        data = json.load(f)
        for pid in range(1, len(data)):
            prompt = data[pid]["prompt"]
            with open(f"/path/to/gemma_7B_codes/{str(pid).zfill(3)}.py", "w") as file:
                file.write(prompt_output(prompt, 512))
                print(f"done for {pid}")

