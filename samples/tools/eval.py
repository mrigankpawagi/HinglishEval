import json
import os
from execution import check_correctness


def evaluate_model(model_name: str) -> float:
    """
    Evaluates the pass@1 score of the model.
    """
    score = 0
    for problem in data:
        task_id = str.zfill(problem["task_id"].split("/")[-1], 3)

        # get completion from samples/sanitized/{model_name}/{task_id}.py
        with open(f"samples/sanitized/{model_name}/{task_id}.py") as f:
            completion = f.read()

        result = check_correctness(problem, completion, 3.0)
        score += 1 if result["passed"] else 0

    return score / len(data)


def evaluate_problemwise(model_name: str) -> list:
    """
    Evaluates problemwise performance of the model. (Function to get data required to run IRT ranking of problems).
    """
    performance_data = []
    for problem in data:
        task_id = str.zfill(problem["task_id"].split("/")[-1], 3)

        # get completion from samples/sanitized/{model_name}/{task_id}.py
        with open(f"samples/sanitized/{model_name}/{task_id}.py") as f:
            completion = f.read()

        result = check_correctness(problem, completion, 3.0)

        if result["passed"]:
            performance_data.append(1)
        else:
            performance_data.append(0)

    return performance_data


if __name__ == "__main__":
    with open("HinglishEval.json") as f:
        data = json.load(f)

    # get all directories in samples/sanitized
    results = {}
    performance_data = {}
    for model_name in os.listdir("samples/sanitized"):
        results[model_name] = evaluate_model(model_name)
        performance_data[model_name] = evaluate_problemwise(model_name)

    # sort the results and print them
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    print(sorted_results)
    print(performance_data)
