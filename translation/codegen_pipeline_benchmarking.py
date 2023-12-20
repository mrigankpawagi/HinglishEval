from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
import threading
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-2B-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-2B-mono")

def gen(prompt):
    generation = pipeline("text-generation", model=model, tokenizer=tokenizer, pad_token_id=50256, temperature=1, max_length=256)
    completion = generation(prompt)[0]['generated_text']
    def sanitize(completion, prompt):
        generated = completion[len(prompt):]
        lines = generated.split("\n")
        final_lines = []
        for l in lines:
            if l.strip() and l[0].strip():
                break
            final_lines.append(l)
        
        return prompt + "\n".join(final_lines)
    print(sanitize(completion,prompt))
prompt= "def has_close_elements(numbers:list[float], threshold:float):\n \"\"\"Diye gaye numbers ki list mein, kya koi do numbers ek dusre se diye gaye threshold se zyada close hain. \n>>> has_close_elements([1.0, 2.0, 3.0], 0.5) \nFalse \n>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) \nTrue \"\"\" "
threads=[]
for i in range(2):
    thread=threading.Thread(target=gen, args=[prompt])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
