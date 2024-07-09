
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
    # TODO: Write your solution here
    # Create a string, check it
    str = file_name
    num_digits = 0
    letter_count = 0
    substring_count = 0
    if '.' not in str[0:3]:
        print("{} is not a valid file/name.".format(file_name))
        return False
    
    for char in str[0:3]:
        if char not in "aA" or char not in "A":
            print("{} not a letter!".format(file_name))
    
    
    if "txt" in str[3:]:
        if not re.match(r"^[a-zA-Z0-9]{2,}\.",str[3:4]):
            print("{} file/name is not a.txt file.".format(file_name))
            return False

    if "exe" in str[3:]:
        if not re.match(r"^[a-zA-Z0-9]{2,}\d+\d+.*",str[3:4]):
            print("{} file/name is not an.