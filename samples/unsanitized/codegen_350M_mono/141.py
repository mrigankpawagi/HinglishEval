
def file_name_check(file_name):
    """
    Ek function banao jo ek string leta hai jisme file ka naam hota hai, aur return karta hai
    'Yes' agar file ka naam valid hai, aur 'No' agar nahi.
    Ek file ka naam tabhi maana jayega jab saare neeche diye gaye conditions meet ho:
    - File ke naam me teen se zyada digits ('0'-'9') nahi hone chahiye.
    - File ke naam me sirf ek dot '.' hona chahiye.
    - Dot se pehle ka substring khali nahi hona chahiye, aur uska shuruat latin alphabet ('a'-'z' aur 'A'-'Z') se hona chahiye.
    - Dot ke baad ka substring inme se ek hona chahiye: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (naam latin alphabet letter se shuru hona chahiye)
    """
    if len(file_name) == 0:
        return False
    elif any(char.isdigit() for char in file_name) == True:
        return False
    else:
        file_name_list = file_name.split('.')
        if len(file_name_list) == 2:
            if file_name_list[1].isalpha() == True:
                return True
            else:
                return False
        else:
            return False
                                                

# Main Method
if __name__ == '__main__':
    
    # Read File
    with open('file.txt', 'r') as file:
        read_data = file.read()
        
    # Check valid_file_data_in_file method
    valid_data = valid_file_data_in_file(read_data)

    # Checking whether valid_file_data_in_file method return True or a tuple
    print