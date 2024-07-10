
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    if file_name.startswith('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return False
    if '.' in file_name:
        return False  
    if not file_name.startswith(file_name.split('.')[-1].lower(), 'txt', 'exe', 'dll').all():
        return False
    if len(file_name.split('.')[-1])>3 or file_name.split('.')[-1]!=file_name.split('.')[-1].lower():
        return False
    return True

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    if file_name.isdigit():
        return False
    if '.' in file_name:
        return False
    substr='',1
    for i in file_name:
        if i.isdigit():
            i=1
        else:
            substr=substr+file_name[i]
        if len(substr)>=3 or substr!=substr.lower():
            return False

    if len(substr)>3 or substr.lower()!=substr:
        return False


##

def is_valid_filename(filename):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file