
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    # Base case: the sequence is already complete
    if (n < 1000):
        return list(np.arange(1,n))
    
    # Find numbers from n
    def find_colt_numbers(n):
        # base case: 1
        if (n == 0) or (isinstance(n, int) and n == 1):
            return [1]
        # Find first number 
        # n.x = n.x + n.x
        first_value = n
        last_value = n
        # Determine how far to take
        while (last_value >= first_value):
            last_value = first_value
            print(n, first_value, last_value)
            if (n % 2) == 0:
                first_value += 1
            else: 
                last_value = n - 1
                
    print("len", len(find_colt_numbers(n)))
    return list(map(find_colt_numbers, [n for n in range(1,1001,2) if isinstance(n, int)]))
            


