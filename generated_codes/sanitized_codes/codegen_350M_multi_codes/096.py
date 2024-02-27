
def count_up_to(n):
    """
    Ek function implement karo jo ek non-negative integer leta hai aur return karta hai ek array jisme pehle n 
    integers hote hai jo prime numbers hai aur n se kam hai.
    Jaise ki:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    k = 0
    n = int(n) # integer n
    if n < 0:
        # if n is negative, return the array without any items
        return [k]
    if k == 0 or k > n:
        # all the items will be counted up to the number given
        return [k] + count_up_to(n)

    # if the number k and the number n is equal, then return the list without any k.
    k = k + 1
    if k == n:
        return [k]
    # if n is not, keep increasing k value
    j = 1 # j
    if n % k == 0:
        # if k is odd, take the first k-1 items
        j -= 1
    j +=1
    # then count all the values from k up to num
    result = [k-j]+count_up_to(n)
    return result
