from transformers import AutoTokenizer, AutoModelForCausalLM
import threading 
import transformers
from packaging import version
assert version.parse(transformers.__version__) >= version.parse("4.23.0")

tokenizer = AutoTokenizer.from_pretrained("NinedayWang/PolyCoder-2.7B")
model = AutoModelForCausalLM.from_pretrained("NinedayWang/PolyCoder-2.7B")
prompt = "def addition(a:int, b:int): return sum of two numbers a and b"

def prompt_output(text):
    print("generating code...")
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    print("a bit more time...")
    # multiple outputs are automatically generated  by giving more max_length. It will abruptly stop in bw a code(last one)
    generated_ids = model.generate(input_ids, max_length=170, pad_token_id=50256)
    print("just itty bitty time more...")
    print(tokenizer.decode(tensor_redefine(generated_ids[0]), skip_special_tokens=True))

def tensor_redefine(tensor):
    tensor_out, pt=[],0
    for ind, token in enumerate(tensor):
        if token==4299:
            pt+=1
            if pt==1:
                tensor_out.append(token)
            else:
                break
        else:
            tensor_out.append(token)
    return tensor_out

threads=[]
for i in range(1):
    thread=threading.Thread(target=prompt_output, args=[prompt])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
## MUCH FASTER than MultipleOutputs.py 