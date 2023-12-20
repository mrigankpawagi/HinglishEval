import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def stableLM_7B(input_prompt):
    tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-zephyr-3b")
    model = AutoModelForCausalLM.from_pretrained("stabilityai/stablelm-zephyr-3b", trust_remote_code=True)

    system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version) is a helpful assistant used for generation of correct codes of docstrings given."""
    prompt = f"{system_prompt}<|USER|>{input_prompt}<|ASSISTANT|>"

    inputs = tokenizer(prompt, return_tensors="pt")
    tokens = model.generate(
    **inputs,
    max_new_tokens=64,
    temperature=0.7,
    do_sample=True,
    )
    print(tokenizer.decode(tokens[0], skip_special_tokens=True))

if __name__ == "__main__":
    prompt="def prime(num:int ): \"\"\" Check if num is prime or not.\"\"\" "
    stableLM_7B(prompt)