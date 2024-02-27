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

def logfile(models):
    # used after every file has log.txt generated from black . &> log.txt in terminal
    with open (f"/Volumes/Anirudh/IISc/DATABASED/labBackup/MultilingualBenchmarking_DBD/{models}/log.txt") as f:
        
        # read each line and search for a 3 digit number
        file= f.readlines()
        error=[]
        for line in file:
            ind= line.find("codes/")
            num= line[ind+6:ind+9]
            print(num)
            if not num.isdigit():
                break
            error.append(int(num))
    return error

def sanitize2(completion, prompt):
    generated=completion[len(prompt):]
    lines = generated.split("\n")
    final_lines = []
    for line in lines:
        if line.strip() and line[0].strip():
            break
        final_lines.append(line)
    return prompt + "\n".join(final_lines)

if __name__ == "__main__":
    import os, json
    models=["codegen_6B_nl_codes", "codegen_6B_mono_codes", "codegen_6B_multi_codes", "codegen_2B_mono_codes", "codegen_2B_multi_codes", "codegen_2B_nl_codes", "codegen_350M_nl_codes", "codegen_350M_mono_codes", "codegen_350M_multi_codes", "codegen2_1B_codes"]
    path_humaneval="/Volumes/Anirudh/IISc/DATABASED/labBackup/MultilingualBenchmarking_DBD/HinglishEval.json"  
    for models in models: 
        try:
            os.mkdir(f"/Volumes/Anirudh/IISc/DATABASED/labBackup/sanitized_codes/{models}")
        except:
            pass
        path_codegen = f"/Volumes/Anirudh/IISc/DATABASED/labBackup/MultilingualBenchmarking_DBD/{models}"
            
        with open(path_humaneval) as f:
            data = json.load(f)
            error=logfile(models)
            for pid in range(len(data)):
                prompt=data[pid]["prompt"]
                entry_point=data[pid]["entry_point"]
                if pid not in error:
                    with open(f"{path_codegen}/{str(pid).zfill(3)}.py") as file:
                        code = file.read()
                    with open(f"/Volumes/Anirudh/IISc/DATABASED/labBackup/sanitized_codes/{models}/{str(pid).zfill(3)}.py", "w") as file:
                        file.write(sanitize1(code, entry_point))
                        print(f"done for {pid}")
                else:
                    with open(f"{path_codegen}/{str(pid).zfill(3)}.py") as file:
                        code = file.read()
                    with open(f"/Volumes/Anirudh/IISc/DATABASED/labBackup/sanitized_codes/{models}/{str(pid).zfill(3)}.py", "w") as file:
                        file.write(sanitize2(code, prompt))
                        print(f"done for {pid}")
                    