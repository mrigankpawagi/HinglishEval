
def f(n):
    """
    Function f ko implement karo jo n ko parameter ke roop mein leta hai,
    aur ek list return karta hai jiska size n hota hai, aisa ki index i par element ka value i ka factorial hota hai agar i even hai
    ya fir 1 se lekar i tak ke numbers ka sum hota hai otherwise.
    i ka start 1 se hota hai.
    i ka factorial 1 se lekar i tak ke numbers ka multiplication hota hai (1 * 2 *... * i).
    Udaharan:
    f(5) == [1, 2, 6, 24, 15]
    """
    if is_prime(n):
        return f(n+1)
    else:
        result = n*f(n-1)
        return result
    return result

print(f(7))

## Ternary Operators

n = 2
# Udaharan:
# result = n+f(n-1)
result = f(n+1)
print(f(n))

# Akhilah:
# print(f(5)) => 6
# f(1) => 1
# f(0) => 1

# Sajna:
# print(f(5)) => 5
# f(2) => 3
# f(3) => 9

# Akhali:
# print(f(5)) => 6
# print(f(6)) => 24
# f(6) => 60
