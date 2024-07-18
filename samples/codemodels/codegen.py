import json
import os

from transformers import AutoModelForCausalLM, AutoTokenizer


def prompt_output(prompt, words):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    # multiple outputs are automatically generated  by giving more max_length. It will abruptly stop in bw a code(last one)
    generated_ids = model.generate(
        input_ids, max_length=words, pad_token_id=50256, do_sample=True
    )
    # print(tokenizer.decode(tensor_redefine(generated_ids[0]), skip_special_tokens=True))
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    path_humaneval = os.path.join(base_dir, "HinglishEval.json")

    codegen_dir = os.path.join(base_dir, "codegen_2B_multi_codes")
    try:
        os.makedirs(codegen_dir, exist_ok=True)
    except:
        pass

    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-2B-multi")
    model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-2B-multi")

    with open(path_humaneval) as f:
        data = json.load(f)
        # for pid in [10, 32, 38, 50]: These pids are special. Take care of them separately
        for pid in range(164):
            prompt = data[pid]["prompt"]
            with open(
                os.path.join(codegen_dir, f"{str(pid).zfill(3)}.py"),
                "w",
            ) as file:
                file.write(prompt_output(prompt, 512))
                print(f"done for {pid}")
