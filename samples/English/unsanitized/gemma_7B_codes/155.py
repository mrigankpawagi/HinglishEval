
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    countTuple = ()
    evenNum = (num % 10) % 10

    if num < 0:
        countTuple = evenNum + 1, (num - 1) % 10

    if num > 0:
        countTuple = evenNum, (num - evenNum) % 10

    return countTuple


print(even_odd_count(-129))
