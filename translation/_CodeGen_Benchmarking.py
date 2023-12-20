from transformers import AutoTokenizer, AutoModelForCausalLM
import threading 
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-2B-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-2B-mono")

def prompt_output(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    # multiple outputs are automatically generated  by giving more max_length. It will abruptly stop in bw a code(last one)
    generated_ids = model.generate(input_ids, max_length=256, pad_token_id=50256, temperature=1)
    print(tokenizer.decode(tensor_redefine(generated_ids[0]), skip_special_tokens=True))

def tensor_redefine(tensor):
    tensor_out,pt = [],0
    for ind, token in enumerate(tensor):
        if token == 4299 and ind > 0 and tensor[ind - 1] == 198:
            pt+=1
            if pt>=2:
                break
            else:
                tensor_out.append(token)
        else: 
            tensor_out.append(token)

    return tensor_out

prompt= "def has_close_elements(numbers:list[float], threshold:float):\n \"\"\"Diye gaye numbers ki list mein, kya koi do numbers ek dusre se diye gaye threshold se zyada close hain. \n>>> has_close_elements([1.0, 2.0, 3.0], 0.5) \nFalse \n>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) \nTrue \"\"\" "

prompt="\n"+prompt
threads=[]
for i in range(2):
    thread=threading.Thread(target=prompt_output, args=[prompt])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
