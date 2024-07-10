import json
import os
import threading

from transformers import AutoModelForCausalLM, AutoTokenizer


def prompt_output(prompt, words):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    # multiple outputs are automatically generated  by giving more max_length. It will abruptly stop in bw a code(last one)
    generated_ids = model.generate(
        input_ids, max_length=words, pad_token_id=50256, do_sample=True
    )
    # print(tokenizer.decode(tensor_redefine(generated_ids[0]), skip_special_tokens=True))
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)


def sanitize(completion, prompt):
    generated = completion[len(prompt) :]
    lines = generated.split("\n")
    final_lines = []
    for line in lines:
        if line.strip() and line[0].strip():
            break
        final_lines.append(line)

    return prompt + "\n".join(final_lines)


if __name__ == "__main__":

    path_humaneval = "/path/to/HinglishEval.json"

    tokenizer = AutoTokenizer.from_pretrained("NinedayWang/PolyCoder-0.4B")
    model = AutoModelForCausalLM.from_pretrained("NinedayWang/PolyCoder-0.4B")

    with open(path_humaneval) as f:
        data = json.load(f)
        for pid in [10, 32, 38, 50]:
            prompt = data[pid]["prompt"]
            with open(
                f"/path/to/polycoder_0.4B_codes/{str(pid).zfill(3)}.py", "w"
            ) as file:
                completion = prompt_output(prompt, 512)
                file.write(sanitize(completion, prompt))
                print(f"done for {pid}")
    print("meow")
    tokenizer = AutoTokenizer.from_pretrained("NinedayWang/PolyCoder-2.7B")
    model = AutoModelForCausalLM.from_pretrained("NinedayWang/PolyCoder-2.7B")

    with open(path_humaneval) as f:
        data = json.load(f)
        for pid in [10, 32, 38, 50]:
            prompt = data[pid]["prompt"]
            with open(
                f"/path/to/polycoder_2.7B_codes/{str(pid).zfill(3)}.py", "w"
            ) as file:
                completion = prompt_output(prompt, 512)
                file.write(sanitize(completion, prompt))
                print(f"done for {pid}")
    tokenizer = AutoTokenizer.from_pretrained("NinedayWang/PolyCoder-160M")
    model = AutoModelForCausalLM.from_pretrained("NinedayWang/PolyCoder-160M")

    with open(path_humaneval) as f:
        data = json.load(f)
        for pid in [10, 32, 38, 50]:
            prompt = data[pid]["prompt"]
            with open(
                f"/path/to/polycoder_160M_codes/{str(pid).zfill(3)}.py", "w"
            ) as file:
                completion = prompt_output(prompt, 512)
                file.write(sanitize(completion, prompt))
                print(f"done for {pid}")

