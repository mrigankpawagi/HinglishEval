from DocstringTranslator import docstring_translator
import openai, threading

openai.api_key = "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"

def function(prompt):
    completion=openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":prompt}])
    # DO not translate the signature of the function
    print("    ", completion.choices[0].message.content)
    # print(docstring_translator(prompt)) though around 80-90% accuracy right now
    return None

prompt = "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n"
threads=[]
for i in range(5):
    thread=threading.Thread(target=function, args=[prompt])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
