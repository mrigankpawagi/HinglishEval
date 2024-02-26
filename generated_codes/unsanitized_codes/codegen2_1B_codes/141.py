
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
    for char in file_name:
        if char not in ascii_letters_to_numbers():
            return 'No'
    return 'Yes'


if __name__ == "__main__":
    input_file = raw_input("Please Input File:\n")
    output_file = raw_input("Please Output File:\n")
    print("Input File: \t", input_file)
    print("Output File: \t", output_file)
    print("input file: \t", file_name_check(input_file))
    print("output file: \t", file_name_check(output_file))
<|python|>import os

from aiogram import filters
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton


class Help(FSMContext):
    def __init__(self, help_data, *args, **kargs) -> None