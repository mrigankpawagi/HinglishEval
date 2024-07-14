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


def sanitize2(completion, entry_point):
    ind = 0
    for typ in ["```python", "```"]:
        if typ in completion:
            ind = completion.find(typ)
            completion = completion[ind + len(typ) :]
            break
    return sanitize1(completion, entry_point)


if __name__ == "__main__":
    import json
    import os

    model = ["llama3_70B"]
    path_humaneval = "/path/to/HinglishEval.json"
    for models in model:
        try:
            os.mkdir(f"/path/to/generated_codes/sanitized/Hinglish/{models}")
        except Exception as e:
            print("Could not make", e)
        path_codegen = f"/path/to/generated_codes/unsanitized/Hinglish/{models}"

        with open(path_humaneval) as f:
            data = json.load(f)
            for pid in range(len(data)):
                entry_point = data[pid]["entry_point"]
                with open(f"{path_codegen}/{str(pid).zfill(3)}.py") as file:
                    code = file.read()
                with open(
                    f"/path/to/generated_codes/sanitized/Hinglish/{models}/{str(pid).zfill(3)}.py",
                    "w",
                ) as file:
                    file.write(sanitize2(code, entry_point))
                    print(f"done for {pid}")

    path_humaneval = "/path/to/HumanEval.json"
    for models in model:
        try:
            os.mkdir(f"/path/to/generated_codes/sanitized/English/{models}")
        except Exception as e:
            print("Could not make", e)

        path_codegen = f"/path/to/generated_codes/unsanitized/English/{models}"

        with open(path_humaneval) as f:
            data = json.load(f)
            for pid in range(len(data)):
                entry_point = data[pid]["entry_point"]
                with open(f"{path_codegen}/{str(pid).zfill(3)}.py") as file:
                    code = file.read()
                with open(
                    f"/path/to/generated_codes/sanitized/English/{models}/{str(pid).zfill(3)}.py",
                    "w",
                ) as file:
                    file.write(sanitize2(code, entry_point))
                    print(f"done for {pid}")
