import os
import csv

from pyirt import irt

from binary_matrix import irt_data as irt_english
from binary_matrix import irt_data2 as irt_hinglish


current_dir = os.path.dirname(os.path.realpath(__file__))


def compute_irt_params(irt_data: list):
    """
    This function is used to compute the Item(problem) and User(model) parameters using the IRT approach.
    :param irt_data : list : A list of tuples containing the model name, problem id and the binary response of the model to the problem.
    """
    item_param, user_param = irt(irt_data)
    return item_param, user_param


def lang_irt():
    """
    Script to compute the IRT parameters for the models in both Hinglish and English. 
    Here both language models are considered in independent IRT evaluations.
    The user and item parameters are stored in a csv file. (./irt_ratings/{lang}_irt_userparams.csv, ./irt_ratings/{lang}_irt_itemparams.csv)
    User parameters : Latency values of the models.
    Item parameters : Difficulty and Discrimination values of the problems.
    """
    for lang in ["Hinglish", "English"]:
        models = []
        data = []
        irt_matrix = irt_english if lang == "English" else irt_hinglish
        sanitized_code_dir = os.path.join(current_dir, f"../samples/{lang}/sanitized")
        for model in os.listdir(sanitized_code_dir):
            model = model.replace(".zip", "") if model.endswith(".zip") else model
            if model in ["codegen2_1B", "santacoder"]:
                continue
            models.append(model)
            for pid in range(164):
                response = irt_matrix[model][pid]
                data.append((model, pid, response))

        item_param, user_param = compute_irt_params(data)

        # with open(f"./irt_ratings/{lang}_irt_userparams.json", "w") as file:
        #    file.write(str(user_param))

        # with open(f"./irt_ratings/{lang}_irt_itemparams.json", "w") as file:
        #    file.write(str(item_param))

        csv_data = [["MODEL", "VALUE"]]
        for model, value in user_param.items():
            csv_data.append([model, f"{value:.3f}"])

        csv_data[1:] = sorted(csv_data[1:], key=lambda x: float(x[1]))
        with open(f"./irt_ratings/{lang}_irt_userparams.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)

        ## Item Parameters
        csv_data = [["PROBLEM", "DIFFICULTY", "DISCRIMINATION"]]
        for problem, value in item_param.items():
            csv_data.append([problem, f"{value['beta']:.3f}", f"{value['alpha']:.3f}"])

        with open(f"./irt_ratings/{lang}_irt_itemparams.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)

        csv_data[1:] = sorted(csv_data[1:], key=lambda x: float(x[2]))
        with open(
            f"./irt_ratings/{lang}_sorted_irt_itemparams.csv", "w", newline=""
        ) as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)


def combined_irt():
    """
    This is for computing the IRT parameters for the models in both Hinglish and English combined in a single evaluation.
    """
    data = []
    models = []
    sanitized_code_dir = os.path.join(current_dir, "../samples/English/sanitized")

    output_name = "Combined"

    for lang in ["Hinglish", "English"]:
        irt_matrix = irt_english if lang == "English" else irt_hinglish
        sanitized_code_dir = os.path.join(current_dir, f"../samples/{lang}/sanitized")
        for model in os.listdir(sanitized_code_dir):
            model = model.replace(".zip", "") if model.endswith(".zip") else model
            if model in ["codegen2_1B", "santacoder"]:
                continue
            models.append(model)
            for pid in range(164):
                response = irt_matrix[model][pid]
                data.append((model + "_" + lang, pid, response))

    item_param, user_param = compute_irt_params(data)
    
    # with open("./irt_ratings/Combined_irt_userparams.json", "w") as file:
    #    file.write(str(user_param))

    # with open("./irt_ratings/Combined_irt_itemparams.json", "w") as file:
    #    file.write(str(item_param))

    # User params
    csv_data = [["MODEL", "VALUE"]]
    for model, value in user_param.items():
        csv_data.append([model, f"{value:.3f}"])

    csv_data[1:] = sorted(csv_data[1:], key=lambda x: float(x[1]))
    with open(
        f"./irt_ratings/{output_name}_irt_userparams.csv", "w", newline=""
    ) as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    ## Item param
    csv_data = [["PROBLEM", "DIFFICULTY", "DISCRIMINATION"]]
    for problem, value in item_param.items():
        csv_data.append([problem, f"{value['beta']:.3f}", f"{value['alpha']:.3f}"])

    csv_data[1:] = sorted(csv_data[1:], key=lambda x: float(x[2]))
    with open(
        f"./irt_ratings/{output_name}_sorted_irt_itemparams.csv", "w", newline=""
    ) as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)


if __name__ == "__main__":
    """
    Run the desired evaluation scripts.
    """
    # lang_irt()
    # combined_irt()
