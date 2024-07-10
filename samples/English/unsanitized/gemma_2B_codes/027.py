

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    
    newString = string.upper()
    for i in range (len(string)):
        # if this string doesnt have a lowercase character 
#         if string[i].islower() == False:       
            #then flip this lowercase character to uppercase
       newString = newString.replace(string[i].lower(), string[i].upper())
    
    return newString
