
def check_dict_case(dict: dict[str, str]):
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
    assert type(dict).__name__ == "dict", "invalid inputs" # $_CONTRACT_$
    keys = list(dict.keys())
    if keys == []: return False
    lower, upper = True, True
    for k in keys:
        if type(k) != str:
            lower = upper = False
            break
        if not k.islower(): lower = False
        if not k.isupper(): upper = False
    return lower or upper

def check(candidate):

    # Check some simple cases
    assert candidate({"p":"pineapple", "b":"banana"}) == True
    assert candidate({"p":"pineapple", "A":"banana", "B":"banana"}) == False
    assert candidate({"p":"pineapple", 5:"banana", "a":"apple"}) == False
    assert candidate({"Name":"John", "Age":"36", "City":"Houston"}) == False
    assert candidate({"STATE":"NC", "ZIP":"12345" }) == True      
    assert candidate({"fruit":"Orange", "taste":"Sweet" }) == True      


    # Check some edge cases that are easy to work out by hand.
    assert candidate({}) == False


check(check_dict_case)