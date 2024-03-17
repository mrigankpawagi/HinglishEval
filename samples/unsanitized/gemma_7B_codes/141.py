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
    if file_name.count(".") > 1:
        return "No"
    if file_name.count(".") == 0:
        return "No"
    if file_name.count(".") == 1:
        if file_name.split(".")[0].isalpha() == False:
            return "No"
        if file_name.split(".")[1] not in ["txt", "exe", "dll"]:
            return "No"
        if file_name.count("0-9") > 2:
            return "No"
        return "Yes"
    return "No"
