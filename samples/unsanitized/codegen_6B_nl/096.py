
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
    prime = [(p[0] - 1, int(p[0]), int(p[1] - 1) + 1) for p in primes()]
    primes = [i for i in range(1, n + 1)]
    for i in range(0, n + 1):  # n is the base array
        if prime[n - i - 1][1] and prime[n - i - 1][0] - 1 not in primes:
            primes.append(prime[n - i - 1])
    res = []
    res.append(prime[0])
    for i, p in enumerate(prime):
        while prime[i][1] and prime[i][0] - 1 not in primes:
            # if prime[i + 1] not in primes[-1]:
            if int(p[1] - 1) - 1 not in primes:
                continue
            res.append(prime[i])