from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, os, json

tokenizer = AutoTokenizer.from_pretrained("bigcode/santacoder")
model = AutoModelForCausalLM.from_pretrained("bigcode/santacoder", trust_remote_code=True)

def sanitize(completion, prompt):
    generated = completion[len(prompt):]
    lines = generated.split("\n")
    final_lines = []
    for line in lines:
        if line.strip() and line[0].strip():
            break
        final_lines.append(line)

    return prompt + "\n".join(final_lines)

def santa_coder(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    generated_ids = model.generate(input_ids, max_length=512, pad_token_id=50256, do_sample=True)

    return sanitize(tokenizer.decode(generated_ids[0]), prompt)

if __name__ == "__main__":
    path_humaneval="/home/admin/AnirudhGupta/MultilingualBenchmarking_DBD/HinglishEval.json"

    with open(path_humaneval) as f:
        data = json.load(f)
        for pid in [10, 32, 38, 50]:
            prompt=data[pid]["prompt"]
            with open(f"/home/admin/AnirudhGupta/MultilingualBenchmarking_DBD/santacoder_codes/{str(pid).zfill(3)}.py", "w") as file:
                file.write(santa_coder(prompt))
                print(f"done for {pid}")
                
 
