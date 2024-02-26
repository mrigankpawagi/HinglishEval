

def sum_to_n(n: int):
    """
    sum_to_n ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    if n==1:
        return 1
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

# Main function call
print("Total Number of Sum is ",sum_to_n(5)) # 7  # Expected output: 47 
# Sum is 47.

###################################################################################
# Number_1

