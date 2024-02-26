
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
    def function_factory(file_name):
        # The first variable is the name of the function or method we want to create
        # The next three variables are the args as we're being called. First argument is
        # the file name.
        # The second argument is True if the name starts with a letter. If it starts with a
        # character and it's not an upper case letter then we don't want to return true.
        # The third argument is the string preceding the first dot.
        # The last argument is the file's extension.
        if re.search("[0-9][0-9][0-9]", file_name):
            return "No"
        else:
            if file_name.startswith(string.ascii_uppercase) == True:
                return "No"
            else:
                # Check the first portion of the file name before the dot.
                filename_before_dot = file_name.split('.', 1)[0]
                if filename_before_dot.startswith("a") == True:
                    return "No"
                elif filename_before_dot.startswith("i"):
                    return "No"