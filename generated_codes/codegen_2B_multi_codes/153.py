
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) =='my_class.AA'
    """
    # Get list of names from names.txt
    names = NamesList('names.txt')
    # Find maximum weight of each extension
    max_w = []
    for name in names:
        # Try to append extension
        if not name.startswith(class_name):
            continue
        # If successful, compare with all other extensions
        for extension in extensions:
            if extension not in name:
                continue
            # Add extension weight to max_w list
            max_w.append(name.strip('.'))
    # Return strong extension
    return max(max_w)


if __name__ == "__main__":
    # Add class names to load
    extension_names = [
        'AAN',
        'ABP',
        'ABWG',
        'ABWT',
        'ABYSW',
        'ABYSWD',
        'ABYSS