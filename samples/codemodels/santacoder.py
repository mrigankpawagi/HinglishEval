import json
import os

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bigcode/santacoder")
model = AutoModelForCausalLM.from_pretrained(
    "bigcode/santacoder", trust_remote_code=True
)


def sanitize(completion, prompt):
    generated = completion[len(prompt) :]
    lines = generated.split("\n")
    final_lines = []
    for line in lines:
        if line.strip() and line[0].strip():
            break
        final_lines.append(line)

    return prompt + "\n".join(final_lines)


def santa_coder(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    generated_ids = model.generate(
        input_ids, max_length=512, pad_token_id=50256, do_sample=True
    )

    return sanitize(tokenizer.decode(generated_ids[0]), prompt)


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    path_humaneval = os.path.join(base_dir, "HinglishEval.json")

    santacoder_codes_dir = os.path.join(base_dir, "santacoder_codes")
    os.makedirs(santacoder_codes_dir, exist_ok=True)

    with open(path_humaneval) as f:
        data = json.load(f)
        for pid in  range (164): # numbers in [10, 32, 38, 50] are special probs
            prompt = data[pid]["prompt"]
            with open(os.path.join(santacoder_codes_dir, f"{str(pid).zfill(3)}.py"), "w") as file:
                file.write(santa_coder(prompt))
                print(f"done for {pid}")
