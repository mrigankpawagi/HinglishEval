from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono", trust_remote_code=True)

def codegen_2B_mono(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    generated_ids = model.generate(input_ids, max_length=256, pad_token_id=50256, temperature=1)
    print(tokenizer.decode(generated_ids[0]))

if __name__ == "__main__":
        prompt="def prime(num:int): \"\"\" Check if given number is prime or not \"\"\" "
        codegen_2B_mono(prompt)