
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
    file_name = file_name.split()
    extension = file_name[-1]
    try:
        assert extension == "txt" or extension == "pdf" or file_name[0] == "."
        for x in file_name:
            if (x == "."):
                pass
            elif re.match(r"[a-zA-Z]+(\.)?") and file_name.index(x) == 0:
                pass
            elif x not in ["txt", "pdf", "md"]:

                return "No"
    except AssertionError:
        return "No"
    return "Yes"


# -----------------------------------------------SOLUTION-------------------------------------------------------

