
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
    for d in dict.keys():
        if d.islower()==False:
            # print("Value ko lower case hai")
            return False
    for a in dict.keys():
        if a.isupper()==False:
            # print("Value ko upper case hai")
            return False
    return True

# Input
print("Enter the name of the dictionary\n")
x = input()
try:
    dct = eval(x)
except(SyntaxError, NameError):
        print("Invalid input")
        exit()

print("Enter the name of the list\n")
y = input()
try:
    lst = eval(y)
except(SyntaxError, NameError):
        print("Invalid input")
        exit()

if dct==None or lst==None:
    print("Invalid input")
    exit()

if len(dct.keys())==len(set(dct.keys())) and len(dct.values())==len(set(dct.values())):
    #print("Dictionary Case valid")
    r=check_dict_case(d