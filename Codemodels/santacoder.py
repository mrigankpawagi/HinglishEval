from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device="cuda:0" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained("bigcode/santacoder")
model = AutoModelForCausalLM.from_pretrained("bigcode/santacoder", trust_remote_code=True)

def santa_coder(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    generated_ids = model.generate(input_ids, max_length=256, pad_token_id=50256, temperature=1).to(device)
    print(tokenizer.decode(generated_ids[0]))
    print("Device: ", device)
if __name__ == "__main__":
        prompt="def prime(num:int): \"\"\" Check if given number is prime or not \"\"\" "
        santa_coder(prompt)
