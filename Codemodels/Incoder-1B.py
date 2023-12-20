import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def incoder_1B(prompt, cuda):
    CUDA = cuda
    model_name = "facebook/incoder-1B"
    kwargs = {}
    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    if CUDA:
        # if you plan to fine-tune the model, you should not use half precision.
        model = model.half().cuda()

    BOS = "<|endoftext|>" # signals the start of a document
    EOM = "<|endofmask|>" # signals the end of a generated infill

    def make_sentinel(i):
        # signals (1) a location to insert an infill and (2) the start of the infill generation
        return f"<|mask:{i}|>"

    def generate(input: str, max_to_generate: int=256, temperature: float=0.2):
        """
        Do standard left-to-right completion of the prefix `input` by sampling from the model
        """
        input_ids = tokenizer(input, return_tensors="pt").input_ids
        if CUDA:
            input_ids = input_ids.cuda()
        max_length = max_to_generate + input_ids.flatten().size(0)
    
        with torch.no_grad():
            output = model.generate(input_ids=input_ids, do_sample=True, top_p=0.95, temperature=temperature, max_length=max_length)
        # pass clean_up_tokenization_spaces=False to avoid removing spaces before punctuation, e.g. "from ." -> "from."
        completion_raw = tokenizer.decode(output.flatten(), clean_up_tokenization_spaces=False)
        if completion_raw.startswith(BOS):
            completion_raw = completion_raw[len(BOS):]
        return completion_raw

    def infill(parts: list[str], max_to_generate: int=128, temperature: float=0.2, extra_sentinel: bool=True, max_retries: int=1):
        assert isinstance(parts, list)
        done=False
        while (not done):

            ## (1) build the prompt
            if len(parts) == 1:
                prompt = parts[0]
            else:
                prompt = ""
                # encode parts separated by sentinel
                for sentinel_ix, part in enumerate(parts):
                    prompt += part
                    if extra_sentinel or (sentinel_ix < len(parts) - 1):
                        prompt += make_sentinel(sentinel_ix)
            
            infills = []
            complete = []
            done = True

            ## (2) generate infills
            for sentinel_ix, part in enumerate(parts[:-1]):
                complete.append(part)
                prompt += make_sentinel(sentinel_ix)
                # TODO: this is inefficient as it requires re-encoding prefixes repeatedly
                completion = generate(prompt, max_to_generate, temperature)
                completion = completion[len(prompt):]
                if EOM not in completion:
                    completion += EOM
                    done = False
                completion = completion[:completion.index(EOM) + len(EOM)]
                infilled = completion[:-len(EOM)]
                infills.append(infilled)
                complete.append(infilled)
                prompt += completion
            complete.append(parts[-1])
            text = ''.join(complete)
        
        return {
            'text': text, # str, the completed document (with infills inserted)
            'parts': parts, # List[str], length N. Same as passed to the method
            'infills': infills, # List[str], length N-1. The list of infills generated
        } 

    def docstring_to_code(max_to_generate=128, temperature=0.2, prompt=format_prompt(prompt)):
        
        parts = prompt.split("<insert>")
        result = infill(parts, max_to_generate=max_to_generate, temperature=temperature)
        print(result["text"])
        return result["text"]
    
    def format_prompt(prompt: str) -> str:

        signature_end_pos = prompt.find('):') + 2
        docstring_start_pos = prompt.find('"""') or prompt.find("'''")

        formatted_prompt =prompt[:signature_end_pos] + '<insert>' + prompt[signature_end_pos:docstring_start_pos] + prompt[docstring_start_pos:]

        prompt="\\\n"+formatted_prompt+"<insert>\n"+"<|/ file |>"
        return prompt
    docstring_to_code()

if __name__ == "__main__":
    prompt = "def has_close_elements(numbers:list[float], threshold:float):\n \"\"\"Diye gaye numbers ki list mein, kya koi do numbers ek dusre se diye gaye threshold se zyada close hain. \n>>> has_close_elements([1.0, 2.0, 3.0], 0.5) \nFalse \n>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) \nTrue \"\"\" "
    incoder_1B(prompt, cuda=False)