import os
import csv
from pyirt import irt
from binary_matrix import irt_data as irt_english
from binary_matrix import irt_data2 as irt_hinglish

current_dir = os.path.dirname(os.path.realpath(__file__))

def compute_irt_params(irt_data: list):
    """
    Compute the Item(problem) and User(model) parameters using the IRT approach.

    :param irt_data: list : A list of tuples containing the model name, problem ID, 
                             and the binary response of the model to the problem.
    :return: tuple : (item_param, user_param)
    """
    return irt(irt_data)

def write_csv(file_path, data):
    """
    Write data to a CSV file.

    :param file_path: str : Path to the CSV file.
    :param data: list : Data to write, where each element is a row.
    """
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def process_irt_data(lang, irt_matrix, sanitized_code_dir):
    """
    Process IRT data for a given language by extracting responses from models.

    :param lang: str : The language being evaluated ("English" or "Hinglish").
    :param irt_matrix: dict : IRT data for the given language.
    :param sanitized_code_dir: str : Path to the sanitized code directory.
    :return: list : Processed IRT data as a list of tuples.
    """
    data = []
    models = []

    for model in os.listdir(sanitized_code_dir):
        model = model.replace(".zip", "") if model.endswith(".zip") else model
        if model in ["codegen2_1B", "santacoder"]:    # Skipt these 2 models. 
            continue
        models.append(model)
        for pid in range(164):
            response = irt_matrix[model][pid]
            data.append((model, pid, response))
    
    return data

def save_irt_results(output_name, item_param, user_param):
    """
    Save IRT results (user parameters and item parameters) to CSV files.

    :param output_name: str : Output name prefix for the CSV files.
    :param item_param: dict : Item parameters with difficulty and discrimination values.
    :param user_param: dict : User parameters with latent values.
    """
    # Save user parameters
    user_csv_data = [["MODEL", "VALUE"]]
    user_csv_data += sorted(
        [[model, f"{value:.3f}"] for model, value in user_param.items()],
        key=lambda x: float(x[1])
    )
    write_csv(f"./irt_ratings/{output_name}_irt_userparams.csv", user_csv_data)

    # Save item parameters
    item_csv_data = [["PROBLEM", "DIFFICULTY", "DISCRIMINATION"]]
    item_csv_data += [
        [problem, f"{value['beta']:.3f}", f"{value['alpha']:.3f}"]
        for problem, value in item_param.items()
    ]
    write_csv(f"./irt_ratings/{output_name}_irt_itemparams.csv", item_csv_data)

    # Save sorted item parameters
    sorted_item_csv_data = [item_csv_data[0]] + sorted(
        item_csv_data[1:], key=lambda x: float(x[2])
    )
    write_csv(f"./irt_ratings/{output_name}_sorted_irt_itemparams.csv", sorted_item_csv_data)

def lang_irt():
    """
    Compute IRT parameters for models in both Hinglish and English, evaluated independently.
    User and item parameters are stored in CSV files.
    """
    for lang, irt_matrix in [("English", irt_english), ("Hinglish", irt_hinglish)]:
        sanitized_code_dir = os.path.join(current_dir, f"../samples/{lang}/sanitized")
        data = process_irt_data(lang, irt_matrix, sanitized_code_dir)
        item_param, user_param = compute_irt_params(data)
        save_irt_results(lang, item_param, user_param)

def combined_irt():
    """
    Compute IRT parameters for models in both Hinglish and English, evaluated jointly.
    Results are saved to CSV files.
    """
    data = []
    for lang, irt_matrix in [("English", irt_english), ("Hinglish", irt_hinglish)]:
        sanitized_code_dir = os.path.join(current_dir, f"../samples/{lang}/sanitized")
        data.extend(process_irt_data(lang, irt_matrix, sanitized_code_dir))
    
    item_param, user_param = compute_irt_params(data)
    save_irt_results("Combined", item_param, user_param)

if __name__ == "__main__":
    """
    Run the desired evaluation scripts.
    Uncomment the desired function calls.
    """
    # lang_irt()
    # combined_irt()
