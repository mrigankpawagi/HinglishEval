
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
    
    # Your code here
    name = extensions[0]
    strength = -1
    for e in extensions:
        if hasattr(class_name, e):
            if strength < 0:
                strength = -1
                name = e
            strength1 = len(e)
            strength2 = len(e.capitalize())
            strength3 = len(e.upper())
            strength4 = len(e.lower())
            strength = strength1 - strength2 + strength3 - strength4
    if strength == -1:
        return class_name
    return class_name + ".%s" % name


from nose.tools import with_setup

@with_setup(print_catastrophic_failure, print_teardown)
