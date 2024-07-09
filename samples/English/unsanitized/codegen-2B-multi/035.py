

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l) if l else None


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # if __name__ == "__main__":
    #     import sys

    #     sys.path.append("../")

    #     import src.utilities
    #     from src.models.base_model import BaseModel

    #     if (sys.version_info >= (3,0,0)):
    #         reload(src)

    #     cls_name = sys.argv[1]
    #     model_name = sys.argv[2]
    #     model_list = {}

    #     model_list[model_name] = []

    #     for model in globals():
    #         if model!= cls_name and hasattr(model, model_name):
    #             model_list[model_name].append(model)
    #     reload(src)

    #     model_path = os.path.join("src", "models", model_name)
