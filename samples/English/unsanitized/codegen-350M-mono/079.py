
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    if decimal is not None:
        l = len(str(decimal//100000000))
        decimal = (decimal%100000000//100000000)%100000000
        if isinstance(decimal, int):
            binary = f'{round(decimal, l)}{round(decimal, l)}'
        else:
            binary = f'{str(decimal)}{round(decimal, l)}{round(decimal, l)}'

        binary = binary[:-l]
        out = ""

        for i in range(len(binary), 0, -1):
            if i//32 == binary.count('1'):
                out += '1'
            else:
                out += '0'

        if out == '':
            return(out)
        else:
            return(f'{out}db{binary[0]}{binary[1]}{binary[-1]}')


