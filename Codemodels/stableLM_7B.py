import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList

def stableLM_7B(input_prompt):
    tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-tuned-alpha-7b")
    model = AutoModelForCausalLM.from_pretrained("stabilityai/stablelm-tuned-alpha-7b")

    class StopOnTokens(StoppingCriteria):
        def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
            stop_ids = set([50278, 50279, 50277, 1, 0])
            return input_ids[0][-1] in stop_ids

    system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version) is a helpful assistant used for generation of correct codes of docstrings given."""
    prompt = f"{system_prompt}<|USER|>{input_prompt}<|ASSISTANT|>"

    inputs = tokenizer(prompt, return_tensors="pt")
    tokens = model.generate(
    **inputs,
    max_new_tokens=64,
    temperature=0.7,
    do_sample=True,
    stopping_criteria=StoppingCriteriaList([StopOnTokens()])
    )
    print(tokenizer.decode(tokens[0], skip_special_tokens=True))

if __name__ == "__main__":
    prompt="def prime(num:int ): \"\"\" Check if num is prime or not.\"\"\" "
    stableLM_7B(prompt)