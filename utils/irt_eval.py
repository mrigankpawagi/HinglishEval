from pyirt import irt
import os

def compute_irt_params(data: list):
    """
    This function is used to compute the Item(problem) and User(model) parameters using the IRT approach.
    :param data: A list of tuples in the format (user_id, item_id, response)
    user_id - ID of the user.
    item_id - ID of the item.
    response - Binary response of the user to the item.
    """
    item_param, user_param = irt(data)
    return item_param, user_param

if __name__ == "__main__":
    data = []
    models =[]
    for model in os.listdir("/samples/sanitized/"):
        models.append(model)
        for pid in os.listdir(f"/samples/sanitized/{model}"):
            with open(f"/samples/sanitized/{model}/{pid}.py", "r") as f:
                response = irt_matrix[model][pid]
                data.append((model, pid, response))
    
    item_param, user_param = compute_irt_params(data)
    print(item_param)
    print(user_param)
    # Use the user_param to obtain the latency of the models.
    # Use the item_param to obtain the difficulty and discriminations of the problems.