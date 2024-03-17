
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
    file_list = []
    for filename in sorted(file_list, key=lambda x: x[0]).reverse()[:]:
        file_name = os.path.getbasename(filename)
        if file_name in file_list:
            file_list.remove(file_name)
            print "Remove old file " + filename
            file_list = []
    return file_list

