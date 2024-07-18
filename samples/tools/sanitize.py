def sanitize1(completion, entry_point):
    anchor = completion.find(f"def {entry_point}")
    x = completion.find("\n", anchor)
    generated = completion[x:]
    lines = generated.split("\n")
    final_lines = []
    for line in lines:
        if line.strip() and line[0].strip():
            break
        final_lines.append(line)
    return completion[: x + 1] + "\n".join([x for x in final_lines if x.strip()])


def logfile(model):
    # Adjusted to dynamically construct the path using __file__
    base_dir = os.path.dirname(__file__)
    log_path = os.path.join(base_dir, "samples", "English", "sanitized", model, "log.txt")
    
    with open(log_path, "r") as f:
        file_lines = f.readlines()
        error = []
        for line in file_lines:
            ind = line.find("codes/")
            if ind != -1:  # Found the substring "codes/"
                num = line[ind + 6: ind + 9]
                if num.isdigit():
                    error.append(int(num))
    return error


def sanitize2(completion, prompt):
    generated = completion[len(prompt) :]
    lines = generated.split("\n")
    final_lines = []
    for line in lines:
        if line.strip() and line[0].strip():
            break
        final_lines.append(line)
    return prompt + "\n".join(final_lines)


if __name__ == "__main__":
    import os, json
    models = ["gpt_4_codes", "gpt_3.5_turbo_codes"]
    base_dir = os.path.dirname(__file__)
    path_humaneval = os.path.join(base_dir, "HinglishEval.json")
    
    for model in models:
        sanitized_codes_dir = os.path.join(base_dir, "samples", "Hinglish", "sanitized", model)
        try:
            os.makedirs(sanitized_codes_dir, exist_ok=True)
        except:
            pass

        with open(path_humaneval) as f:
            data = json.load(f)
            error = logfile(model)
            for pid in range(len(data)):
                prompt = data[pid]["prompt"]
                entry_point = data[pid]["entry_point"]
                path_codegen = os.path.join(base_dir, model)
                sanitized_file_path = os.path.join(sanitized_codes_dir, f"{str(pid).zfill(3)}.py")
                
                if pid not in error:
                    code_file_path = os.path.join(path_codegen, f"{str(pid).zfill(3)}.py")
                    with open(code_file_path) as file:
                        code = file.read()
                    with open(sanitized_file_path, "w") as file:
                        file.write(sanitize1(code, entry_point))
                        print(f"done for {pid}")
                else:
                    code_file_path = os.path.join(path_codegen, f"{str(pid).zfill(3)}.py")
                    with open(code_file_path) as file:
                        code = file.read()
                    with open(sanitized_file_path, "w") as file:
                        file.write(sanitize2(code, prompt))
                        print(f"done for {pid}")    
