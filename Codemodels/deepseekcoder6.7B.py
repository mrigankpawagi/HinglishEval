from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def deepseekcoder(prompt: str, device):

    tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-6.7b-base", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-6.7b-base", trust_remote_code=True, torch_dtype=torch.bfloat16)

    input_text = prompt
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_length=128)

    completion=tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(completion[len(input_text):])

if __name__=="__main__":
    #writing system prompt is important before docstring
    system_prompt = " Write a code for the following docstring."
    instruction="def perfectsq(num:int):\n \"\"\" Returns True if num is a perfect square, else False \"\"\""
    device="cpu"
    deepseekcoder(system_prompt+instruction, device)