

def change_base(x: int, base: int):
    """
    Input number x ka numerical base, base me badal do.
    Conversion ke baad string representation return karo.
    Base numbers 10 se kam hote hain.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if type(base) !=int or base>10:
        return ('Enter a positive integer less than 10.\n')
    if type(x) != int or x < base:
        return 'Input should be a integer which' +  ' must greater than or equal to' +" base number."
    number = int(x)
    if number < base:
        return str(number)
    string = change_base(number//base, base)
    string = string + str(number % base)
    
    return string
