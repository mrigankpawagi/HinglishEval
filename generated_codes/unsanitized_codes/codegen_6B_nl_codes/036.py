

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
    count = 0
    return sum(
        a == 7 if a == int(a) else a % 3 + 1 for a in str(n)
    )

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    for i in range(n + 1):
        for j in range(i + 1):
            if  fizz_buzz(n) == i + 1:
                print("fizz")
                n -= 1 # decrement n for next case
                print("buzz")

            elif fizz_buzz(n) == j + 1:
                print("fizz")
                print("buzz")
                n -= 1 # decrement n for next case
                print("fizz")
                print("buzz")

            else:
                print("fizz")
                print("