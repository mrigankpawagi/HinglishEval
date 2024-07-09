
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
    file_name_re = re.compile("^[0-9]{3,4}(?:\\.[a-z]{2})*[a-z0-9]\\.[a-z]{2,4}$")

    def file_name_func(s):
        if file_name_re.match(s):
            return 'Yes'
        else:
            return 'No'

    return file_name_func

if __name__ == "__main__":
    file_name = eval(input("Enter 3-10-20 digits file name or '-' to go back to main menu: "))
    if file_name!= '-':
        validation = file_name_check(file_name)
        if validation == 'Yes':
            print('Your file name is valid!')
            exit()
        else:
            exit()