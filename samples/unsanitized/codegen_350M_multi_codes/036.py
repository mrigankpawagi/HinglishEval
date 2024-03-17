

def fizz_buzz(n: int):
    """
    n se kam integers mein, jo 11 ya 13 se divisible hain, usme digit 7 kitni baar aata hai, uska count return karo.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n <= 1:
        return
    fizz=[]
    buzz=[]
    for i in range(1,n):
        buzz_array = [False] * (n-1) # array of booleans
        if i == 1:
            buzz_array[0] = True # aa
        fizz_buzz_array=  buzz_array[n-1]
        fizz_buzz_array = fizz_buzz_array[:i] # remove old elements from fizz
        fizz.append(fizz_buzz_array)

    if len(fizz) <= 1: #if len(fizz)==1: #se hai kama nie usem, jak hane nie hain
        return fizz[0]

    elif len(fizz)==1: #se hai kama nie usem, kama fizz=n-1 usme
        return fizz[-1]
    elif len(fizz)<=len(fizz)-1: #falsy output?
        return fizz[max(0,len(fizz)-1)]

    else:
        #se fizz array se han wye aa
        return [fizz_buzz_array[i] for i in range(0,len(fizz))]

#se ouput 1, 2, 3, and 4 is in array fizz[i]
#se ouput array fizz_i, fizz_array_se, fizz_buzz_array_se
