

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factors = [] ## List in which we will store all the possible prime factors
    while n % 2 == 0: ## While we are at the end of the loop
        prime_factors.append(2) ## Add the two squares of prime factors in one list
        n = n/2 ## Update the number
    for p in range(3, n, 2):
            i = 0 # i should be at the lowest possible factor
            while(p % p == 0):
                p = p/pow(2, i) ## Recursively call this function till we find the factors
                i = i + 1
    if len(prime_factors) > 10: # The above if/else statement is to reduce the number of possible prime factors after 10
        prime_factors = prime_factors[:min(len(prime_factors), 10)]
    # Now our possible prime factors are obtained.
    # Let's build an index of each element in the array and then append its indexes to our prime factor array
    index = [i for i in range(len(prime_factors))]
    a = 0 # A counter variable keeps track of the current index inside the array
    b = len(prime_factors) - 1 # B counter variable keeps track of the index where the next possible factor ends

    while a < b :
        # Let's loop through all the elements in our array of prime factors so far
        while (prime_factors[a]!= prime_factors[b]):
            if prime_factors[a] < prime_factors[b]:
                a = a + 1
            else:
                b = b -1
        # For the possible next factor, add the new index to the list and the remaining index to the previous index.
        index[b] = a
        a = a + 1
        b = b -1
    # We got all the possible prime factors so let's print it out.
    return