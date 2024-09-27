import os

from pyirt import irt

from binary_matrix import irt_data as irt_english
from binary_matrix import irt_data2 as irt_hinglish


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


if __name__ == "__main__":
    data = []
    models = []
    # get the filepath of tihs code
    current_dir = os.path.dirname(os.path.realpath(__file__))
    for lang in ["Hinglish", "English"]:
        irt_matrix = irt_english if lang == "English" else irt_hinglish
        sanitized_code_dir = os.path.join(current_dir, f"../samples/{lang}/sanitized")
        for model in os.listdir(sanitized_code_dir):
            model = model.replace(".zip", "") if model.endswith(".zip") else model
            if model in ["codegen2_1B"]:
                continue
            models.append(model)
            for pid in range(164):
                response = irt_matrix[model][pid]
                data.append((model, pid, response))

        item_param, user_param = compute_irt_params(data)
        print(item_param)
        print(user_param)
    # Use the user_param to obtain the latency of the models.
    # Use the item_param to obtain the difficulty and discriminations of the problems.
