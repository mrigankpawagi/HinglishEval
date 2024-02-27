
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
    a = []  # list for storing the keys of the key
    b = []  # list for storing the value

    for i, kv in enumerate(dict.keys()):
        if str.islower(kv):  # if keys is lower case string
            a.append(kv)  # then append keys to a list
            b.append(dict[kv])  # else add value of dict to b
        elif str.istitle(kv):  # if keys is a Title Case string
            b.append(dict[kv])  # else add value of dict to b
        else:  # if keys is both case insensitive and upper case
            pass
    return a == b  # is the length of keys matching the length of values
