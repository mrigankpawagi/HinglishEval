from transformers import AutoTokenizer, AutoModelForCausalLM
import threading 
import transformers
from packaging import version
assert version.parse(transformers.__version__) >= version.parse("4.23.0")

tokenizer = AutoTokenizer.from_pretrained("NinedayWang/PolyCoder-2.7B")
model = AutoModelForCausalLM.from_pretrained("NinedayWang/PolyCoder-2.7B")
prompt = "def addition(a:int, b:int): return sum of two numbers a and b"

def polycoder(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    generated_ids = model.generate(input_ids, max_length=170, pad_token_id=50256)
    print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))

if __name__=="__main__":
    prompt="def prime(num:int): \"\"\" Check if number given is prime or not. \"\"\" "
    print(polycoder(prompt))