
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift < 0:
        return "".join(chr(int(x, base)) for x in reversed(x))
    else:
        return "".join(chr((p % 10) + shift) if p<10 else chr(11 + shift) for p in x)

It does not take into account overflow or underflow, which is usually done at runtime with one of the "round" functions:

round(a, b)
round(a, b, n)

Or, if you are using Python 2:

round(a, b, n)
round()

The problem with the circular_shift function is that it does not take into account the end of the string being appended. For example,
for i in range(100):
    print(circular_shift("", -1))

will result in:
3   9   21   45   27   23   11   33   12

whereas the correct answer to the same problem in my answer requires the trailing spaces at the end of the string:
3   9   21   45   27   23   11   33   12 

I am not sure how good or bad this is. It might even be desirable to have a more rigorous way of achieving that effect.

