from transformers import pipeline
import torch

device="cuda:0" if torch.cuda.is_available() else "cpu"
MAGICODER_PROMPT = """You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Instruction
{instruction}

@@ Response
"""

instruction = "def has_close_elements(numbers:list[float], threshold:float):\n \"\"\"Diye gaye numbers ki list mein, kya koi do numbers ek dusre se diye gaye threshold se zyada close hain. \n>>> has_close_elements([1.0, 2.0, 3.0], 0.5) \nFalse \n>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) \nTrue \"\"\" "

prompt = MAGICODER_PROMPT.format(instruction=instruction)
generator = pipeline(
    model="ise-uiuc/Magicoder-S-DS-6.7B",
    task="text-generation",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
result = generator(prompt, max_length=2048, num_return_sequences=1, temperature=0.0)
print(result[0]["generated_text"])