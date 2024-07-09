
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
    # Returns True if the file's name is valid, False otherwise.
    valid_file_name = False
    # Check whether the name starts with valid character.
    if '.' in file_name:
        valid_file_name = True
        # Extract characters after the dot. They might contain a letter from the latin alphabet.
        letters_after_dot = file_name[file_name.rfind('.')+1:]
    else:
        letters_after_dot = 'None'
    if len(characters) < 3:
        valid_file_name = False
    # Check if the file's name contains exactly one character, that comes from alphapete ('A'-Z and 'a'-'z')
    characters = char_valid_chars('A'-'Z', 'a'-'z')
    if not valid_file_name and (len(