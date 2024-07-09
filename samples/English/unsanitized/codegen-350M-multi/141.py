
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
    def f(file_name):
        if '\0' in file_name and not '\0' in file_name.replace('\\', ''):
            return False, '\0'
        new_file_name = file_name.replace('\\', '')
        is_valid, new_file_name_part = file_name_check(new_file_name_part)
        return is_valid, new_file_name_part

    return f


class File():
    """Class that wraps os.path objects. The only thing it acts
    is to determine whether a filename is valid or not.
    It's also used when the current system's default
    encoding is set to utf-8.
    """
    def __init__(self,
                 filename_or_file_system_directory = None,
                 file_name_function = None):
        try:
            if file_name_function is not None and not callable(file_name_function):
                raise Exception("file_name_function can't be a string when calling the class")
        except Exception as e:
            raise Exception("Failed with %s exception: '%s'" % (