
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
    if bool(dict) == False:
        return False
    else:
        return all((isinstance(dict[x], str), dict[x].lower() == dict[x].lower() and dict[x].upper()!= dict[x].upper()) for x in dict)

##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################

print('\n' + str('='*3) +'Test case 2.1 of check_dict_case' + str('='*3) + '\n')

my_dict = {
    'a': 'apple',
    'b': 'banana'
}
print('Expected: ', True)
print('Actual = ', check_dict_case(my_dict))


##############################

print('\n' + str('='*3) +'Test case 2.2 of check_dict_case' + str('='*3) + '\n')

my_dict = {
    'A': 'apple',
    'b': 'banana',
    'a': 'apple'
}
print('Expected False')
print('Actual is ', check_dict_case(my_dict))

##############################

print('\n' + str('='*3)