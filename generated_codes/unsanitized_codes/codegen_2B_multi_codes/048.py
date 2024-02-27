def is_palindrome(text: str):
    """
    Diye gaye string ko check karta hai ki kya yeh palindrome hai
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    if text[:1] != text[-1:]:
        return False
    for i, b in enumerate(text[1:-1] * 2 - 1):
        if text[i] != b:
            sys.exit(1)
    return True


with open("data/day8-3.txt", "r") as f:
    data = f.read()

result = [""]
for l in data.split():
    s = [l]
    n = []
    for i in range(1, len(l)):
        n.append(s[i : i + 2])
        a = sum(n) + s[i - 1]
        b = sum(n) - s[i - 1]
        while a < b:
            a += sum(n[:-1])
            b -= sum(n[:-1])
        a /= 2
        b /= 2
        s.append(a + b)
    result.append("".join(s))

for s in result:
    if is_palindrome(s):
        print(s)
        exit()
