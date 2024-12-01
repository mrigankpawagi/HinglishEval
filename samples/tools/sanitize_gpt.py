import json
import os


def sanitize1(completion, entry_point):
    anchor=completion.find(f"def {entry_point}")
    x=completion.find("\n",anchor)
    generated = completion[x:]
    lines = generated.split("\n")
    final_lines = []
    for line in lines:
        if line.strip() and line[0].strip():
            break
        final_lines.append(line)
    return completion[:x+1] + "\n".join([x for x in final_lines if x.strip()])

def sanitize2(completion, entry_point):
    ind=completion.find("```python")
    completion=completion[ind+9:]
    return sanitize1(completion,entry_point)

if __name__ == "__main__":
    model_list = ["gpt_4_codes", "gpt_3.5_turbo_codes"]
    base_dir = os.path.dirname(__file__)
    path_humaneval = os.path.join(base_dir, "HinglishEval.json")
     
    for model in model_list:
         
        sanitized_codes_dir = os.path.join(base_dir, "samples", "Hinglish", "sanitized", model)
        try:
            os.makedirs(sanitized_codes_dir, exist_ok=True)
        except Exception as e:
            print("Error: ", e)

        path_codegen = os.path.join(base_dir, model)
        with open(path_humaneval) as f:
            data = json.load(f)
            for pid in range(len(data)):
                entry_point=data[pid]["entry_point"]
                with open(f"{path_codegen}/{str(pid).zfill(3)}.py") as file:
                    code = file.read()
                    
                sanitized_file_path = os.path.join(sanitized_codes_dir, f"{str(pid).zfill(3)}.py")
                with open(sanitized_file_path, "w") as file:
                    file.write(sanitize2(code, entry_point))
                    print(f"done for {pid}")
