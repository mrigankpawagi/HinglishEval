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
    # your code here
    if len(file_name) > 3:
        return "No"
    if (
        file_name[0] != "a"
        and file_name[0] != "A"
        and file_name[0] != "0"
        and file_name[0] != "1"
        and file_name[0] != "2"
        and file_name[0] != "3"
        and file_name[0] != "4"
        and file_name[0] != "5"
        and file_name[0] != "6"
        and file_name[0] != "7"
        and file_name[0] != "8"
        and file_name[0] != "9"
    ):
        return "No"
    if file_name[1] != ".":
        return "No"
    if file_name[2] != "txt" and file_name[2] != "exe" and file_name[2] != "dll":
        return "No"
    return "Yes"
