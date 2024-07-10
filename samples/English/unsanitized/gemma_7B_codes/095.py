
def check_dict_case(dict):
    """
    Ek dictionary di gayi hai, return karo True agar saare keys lower case strings hai ya saare keys upper case strings hai, nahi to return karo False.
    Agar di gayi dictionary khali hai to function False return karega.
    Udaharan:
    check_dict_case({"a":"apple", "b":"banana"}) ka return hona chahiye True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) ka return hona chahiye False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) ka return hona chahiye False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) ka return hona chahiye False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) ka return hona chahiye True.
    """
    if dict is None or len(dict) == 0:
        return False
    for key, val in dict.items():
        # print(key.lower(), key.upper(), type(key.lower()) == type(key.upper()))
        if type(key.lower()) == type(key.upper()): continue
        else: return False
    return True

print(check_dict_case({"test_1":"apple", "test_2":"banana", "test_3":"kiwi"}))
