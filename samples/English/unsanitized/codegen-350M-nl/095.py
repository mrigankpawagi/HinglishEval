
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    k,d=key(dict)
    if not isattr(d, "dict_case"):
        return False  
    other = d[k, 1], d[k, 0]
    if d == "dict_case":
        if other!= "dict_case": 
            return False    # True.  
        return k                  #False
    elif isinstance(d"dict_case" or d) and k in ("a", "B"):
        return k!= ".ab"     # True
    elif isinstance(d, "dict" + str) and k in ("a", "B", "ab"):
        return k!= ".ab"
    elif k in ("A", "A,B,C"):
        return k!= ".ab"
    elif isinstance(d, "dict" + str):
       