
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
    def check_dict_case_v(d):
        for key in d:
            if type(d[key]) != str:
                return False
        for key in d:
            if d[key].isupper() or d[key].islower():
                continue
        return False
    return check_dict_case_v(dict)

if __name__ == "__main__":
    res = check_dict_case({"a":"apple", "b":"banana"})
    assert res == True, "Should return True when keys are all strings in lower case."
    res = check_dict_case({"a":"apple", "A":"banana", "B":"banana"})
    assert res == False, "Should return False when keys are all strings in upper case."
