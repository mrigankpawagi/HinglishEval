
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
    if not isinstance(file_name,basestring):
        raise ValueError, "file_name must be string"
    if not len(file_name):
        raise ValueError, "file_name required"
    if not file_name[-4:].lower() in ['txt','exe','dll']:
        return 'No'
    try:
        is_good_name = True
        for i in file_name:
            if not '0' <= i <= '9':
                is_good_name = False
                break
        if is_good_name:
            return 'Yes'
    except:
        return 'No'
    return 'No'

