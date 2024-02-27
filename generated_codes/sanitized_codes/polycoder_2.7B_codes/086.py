def anti_shuffle(s):
    """
    Ek function likho jo ek string leta hai aur uska ordered version return karta hai.
    Ordered version of string, woh string hoti hai jahan saare words (space se separated)
    ko ek naye word se replace kiya jata hai jahan saare characters ko
    unke ascii value ke basis pe ascending order mein arrange kiya jata hai.
    Dhyan do: Aapko words aur blank spaces ki order sentence mein maintain karni chahiye.

    Jaise ki:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    i = s.find(" ")
    j = s.find(" ", i)

    k = min(i, j)
    a = s[k:].lower()
    aa_aa = "".join(a.split(" "))
    aa_aa = "".join(aa_aa.split())
    aax = k - k % 2 + 1
    bah = s[ax:].strip()
    bah = "".join(bah.split())
    bah = bah.lower()

    return aa_aa + aax + bah
