

def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    print("N")

    if n > 20_000_000_000:
        print("hi")
        return n
    if n > 3_000_000_000_000:
        print("hi")
        return n
    if n % 4_000_000_000 <= 1:
        print("hi")
        return n
    for i in range(1, n + 1):
        if (n % i) == 0:
            return i
    print(n)


if __name__ == "__main__":
    largest_divisor(15)
<|python|>)
        n1 += 0.5*dt*np.sin(2*np.pi*2*n*t1*x/5)**3
        n2 -= 0.5*dt*np.sin(2*np.pi*2*n*t2*x/5)**3
    return n1,n2


