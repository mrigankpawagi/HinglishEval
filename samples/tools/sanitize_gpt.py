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
    import os, json
    models=["gpt_4_codes", "gpt_3.5_turbo_codes"]
    path_humaneval="/Volumes/Anirudh/IISc/DATABASED/labBackup/MultilingualBenchmarking_DBD/HinglishEval.json"  
    for models in models: 
        try:
            os.mkdir(f"/Volumes/Anirudh/IISc/DATABASED/labBackup/generated_codes/sanitized_codes/{models}")
        except:
            pass
        path_codegen = f"/Volumes/Anirudh/IISc/DATABASED/labBackup/MultilingualBenchmarking_DBD/{models}"
            
        with open(path_humaneval) as f:
            data = json.load(f)
            for pid in range(len(data)):
                entry_point=data[pid]["entry_point"]
                with open(f"{path_codegen}/{str(pid).zfill(3)}.py") as file:
                    code = file.read()
                with open(f"/Volumes/Anirudh/IISc/DATABASED/labBackup/generated_codes/sanitized_codes/{models}/{str(pid).zfill(3)}.py", "w") as file:
                    file.write(sanitize2(code, entry_point))
                    print(f"done for {pid}")
