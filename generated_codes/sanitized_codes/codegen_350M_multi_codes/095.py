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
    karega = False
    for k in dict.keys():
        if type(dict[k]) is str:
            a = dict[k].upper()
            if a.isdigit() and len(a) > 0 and (a == dict[k] + "#"):
                karega = True
            elif a.isalnum():
                if k not in ("City", "C") and k not in ("State", "ST"):
                    karega = True
        else:
            if type(dict[k]) is list:
                if dict[k][0] in ("Apple", "Banana"):
                    ka = False
            else:
                if k in ("City", "State", "ZIP"):
                    ka = False
            # Check karyoku karega
            if not karega:
                if ka:
                    karega = False
        if karega == False:
            return karega
    return karega