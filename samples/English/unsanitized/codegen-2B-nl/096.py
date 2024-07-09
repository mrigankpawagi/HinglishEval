
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    if n <= 0:
        return []
    if n in primes:
        result = n
    else:
        result = [n]
    while True:
        new = []
        if n > 0:
            for prime in primes:
                n = n // prime
                if n == 0:
                    new.append(n)
            new += [(n+1)]
        else:
            result = result + new                
        elif n < n ** 0.5:
            if n not in sum_nums:
                sum_nums.append(n)

    return result

if __name__ == "__main__":
    primes