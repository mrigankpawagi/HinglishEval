
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
    if not isinstance(dict,Mapping) or not all(isinstance(x,str) and isinstance(x.lower(),str)or isinstance(x.upper(),str)or not isinstance(x,unicode) ):
        return False
    else:
        if "STATE" not in dict and "AUTHORITY" not in dict and "NAME" not in dict and "ID" not in dict and "_" not in dict and None not in dict:
            return False
        else:
            return True

Then this code:
df["a"].map(lambda x: check_dict_case(df["Data"])) should work but I am looking for more pythonic way.

A:

You can use Python's built-in filter function to filter df["Data"] according to check_dict_case, then use map to apply the check_dict_case function to each individual column in the DataFrame as its name argument:
df["a"] = df["Data"].filter(lambda x: check_dict_case(x))\
   .map(lambda