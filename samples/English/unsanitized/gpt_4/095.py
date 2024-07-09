def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    if all(isinstance(key, str) and key.islower() for key in keys):
        return True
    elif all(isinstance(key, str) and key.isupper() for key in keys):
        return True
    else:
        return False