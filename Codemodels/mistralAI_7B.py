# This is mistralai/Mistral-7B-Instruct-v0.2
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def mistralAI(prompt: str, device):
    model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

    messages = [
        {"role": "user", "content": "def prime(num:int): \"\"\" Returns True if num is prime, else False \"\"\""},
        {"role": "assistant", "content": "def prime(num:int): \"\"\" Returns True if num is prime, else False \"\"\" \n return num > 1 and all(num % i != 0 for i in range(2, num))"},
        {"role": "user", "content": prompt}
    ]

    encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

    model_inputs = encodeds.to(device)
    model.to(device)

    generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
    decoded = tokenizer.batch_decode(generated_ids)
    print(decoded[0])

if __name__=="__main__":
    prompt = "def perfectsq(num:int): \"\"\" Returns True if num is a perfect square, else False \"\"\""
    #device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    mistralAI(prompt, "cpu")