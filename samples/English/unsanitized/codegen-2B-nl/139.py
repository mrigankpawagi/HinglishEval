
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    retVal = 1 # initialize result
    if not isInt(n):
        raise ValueError
    
    prevLastValidCount = -1
    prevLastValidInt = int(n)
    for _ in range(100): # skip to 100 so if it rounds back to itself
        try:
            val = int(n) # Try to get the integer as an int
        except ValueError:
            retVal = 0 # If the integer is not in the range of a valid integer as int then return 0 (zero)
            raise ValueError
          
        if not val:
            break

        if val == 1: # For special cases: 1, -1
            prevLastValidInt = int(val)
        prevLastValidCount = int(n) # Prev count of previous successful rounds
        if prevLastValidCount % 2 == 0 and (val!= 1):
            retVal = int(special_factorial(prevLastValidInt)+int(pow(val-1, prevLastValidCount))) # Special case for -n (not in range)
        elif prevLastValidCount % 2 == 0:
         