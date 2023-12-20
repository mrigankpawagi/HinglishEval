from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device="cpu"
tokenizer = AutoTokenizer.from_pretrained("WizardLM/WizardCoder-Python-7B-V1.0")
model = AutoModelForCausalLM.from_pretrained("WizardLM/WizardCoder-Python-7B-V1.0", trust_remote_code=True)

def wizard_coder(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    generated_ids = model.generate(input_ids, max_length=256, pad_token_id=50256, temperature=1).to(device)
    print(tokenizer.decode(generated_ids[0]))
    print("Device: ", device)

if __name__ == "__main__":
        instruction="def prime(num:int): \"\"\" Check if given number is prime or not \"\"\" "
        prompt=f"Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Response:"
        wizard_coder(prompt)
