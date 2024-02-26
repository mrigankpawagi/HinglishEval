

def encode_shift(s: str):
    """
    Har character ko alphabet mein 5 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    return "".join(chr(ord(ch) -((26 -(ord(ch) + 5 - ord("a"))) % 26) + ord("a")) + ch for ch in s)

t=int(input())
for t in range(t):
    n=input()
    a={}
    for i in range (n):
        n=input()
        s=str(n)
        s=encode_shift(s)
        for j in range(n):
            m=input()
            s=str(encode_shift(s))
            m=decode_shift(s)
            a.setdefault(m,set()).add(j)
    t=max(a.values())
    if "a" in a.keys():
        a.pop("a")
    n=t
    if a:
        print(max(a.keys()))
    else:
        print('none')
