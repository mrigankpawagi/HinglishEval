import json
import os


def extract_prompt_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    # Split the content using triple double quotes
    parts = content.split('"""')
    return '"""\n    ' + parts[3].strip() + '\n    """'


def hinglish_json():
    # File path to the JSON file
    base_dir = os.path.dirname(__file__)
    path_humaneval = os.path.join(base_dir, "HumanEval.jsonl")
    with open(path_humaneval, "r") as json_file:
        data = json.load(json_file)

    # modify the data with the hinglish prompts
    new_data, index = [], 0
    for item in data:
        i = item["task_id"].split("/")[1]
        prompt = extract_prompt_from_file(f"drafts/{i}")  # original prompt

        prev_prompt = item[
            "prompt"
        ]  # changing only the docstring not the function signature
        entry_point = item["entry_point"]

        if '"""' in prev_prompt:
            index = prev_prompt.index('"""', prev_prompt.index(entry_point))
        elif "'''" in prev_prompt:
            index = prev_prompt.index("'''", prev_prompt.index(entry_point))

        # overwriting the orginal prompt. also if the new docstring is longer than the slice it isnt an issue as the string length is changed in-place
        item["prompt"] = item["prompt"][:index] + prompt

        new_data.append(item)

    # write the new data to the json file
    with open("../HinglishEval.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    hinglish_json()
