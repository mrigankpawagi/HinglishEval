from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device="cuda:0" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained("bigcode/starcoderbase-3b")
model = AutoModelForCausalLM.from_pretrained("bigcode/starcoderbase-3b")

def codegen_2B_mono(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    generated_ids = model.generate(input_ids, max_length=256, pad_token_id=50256, temperature=1)
    print(tokenizer.decode(generated_ids[0]))

if __name__ == "__main__":
        prompt="def prime(num:int): \"\"\" Check if given number is prime or not \"\"\" "
        codegen_2B_mono(prompt)