
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
    odd_collatz = []
    i = 1
    while i <= n or i!= 1:
        if i % 2 == 0:
            odd_collatz.append(i)
        else:
            x = i >> 1
            odd_collatz.append(int(math.pow(x, 2)))
        i += 1
    odd_collatz.insert(0, 1)  # Add one as first integer to get [1, 5] for example. 

    for j in range(3, len(odd_collatz)):  # 3 is the start point for the step above. 
        new_odds = []
        for k in range(len(odd_collatz)):
            new_odds.append(int(odd_collatz[k] // 2))
        odd_collatz = new_odds

    return odd_collatz


if __name__ == "__main__":
    print(get_odd_collatz(4))