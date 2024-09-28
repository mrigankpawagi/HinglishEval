import os
import csv

from pyirt import irt

from binary_matrix import irt_data as irt_english
from binary_matrix import irt_data2 as irt_hinglish


current_dir = os.path.dirname(os.path.realpath(__file__))


def compute_irt_params(irt_data: list):
    """
    This function is used to compute the Item(problem) and User(model) parameters using the IRT approach.
    :param data: A list of tuples in the format (user_id, item_id, response)
    user_id - ID of the user.
    item_id - ID of the item.
    response - Binary response of the user to the item.
    """
    item_param, user_param = irt(irt_data)
    return item_param, user_param


def lang_irt():
    # get the filepath of tihs code
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
        # add user_param in json formatted style in a new file, user_param.json
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
    # Use the user_param to obtain the latency of the models.
    # Use the item_param to obtain the difficulty and discriminations of the problems.


def combined_irt():
    ## COMBINED
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
    # lang_irt()
    combined_irt()
