
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
    for key in dict:
        if len(key) == 1:
            print "\nKey: ", key, "Name:", key.lower(), "Name: ", key.upper(), "Value: "
        elif len(key) == 2:
            print "\nKey: ", key, "Name:", key.lower(), "Name: ", key.upper(), "Value: "
    return
    #if (len(key) == 1):
        #if ((key == "ZIP")) | (key == "ZIPCODE") | (key == "ZIP_NAME") :
            #print "\nKey: ", key, "Name:", key.lower(), "Name: ", key.upper(), "Value: "
        #if not ((key == "City") | (key == "STATE") | (key == "CITY") | (key == "STATE") | (key == "STATE_NAME") | (key == "STATE_NAME")) :
            #print "\nKey: ", key, "Name:", key.lower(), "Name: ", key.upper(), "Value: "
    #elif (len(key) == 2):
        #if