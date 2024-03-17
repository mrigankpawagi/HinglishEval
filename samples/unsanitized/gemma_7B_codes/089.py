def encrypt(s):
    """
    Ek function banaiye encrypt jo ek string ko argument ke roop mein leta hai aur
    ek encrypted string return karta hai jisme alphabet ko rotate kiya gaya ho.
    Alphabet ko aise rotate karna chahiye ki letters
    do se multiply kiye gaye do places ke neeche shift ho jaye.
    Jaise ki:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    # your code here
    s = s.lower()
    s = s.replace(" ", "")
    s = s.replace("a", "z")
    s = s.replace("b", "y")
    s = s.replace("c", "x")
    s = s.replace("d", "w")
    s = s.replace("e", "v")
    s = s.replace("f", "u")
    s = s.replace("g", "t")
    s = s.replace("h", "s")
    s = s.replace("i", "r")
    s = s.replace("j", "q")
    s = s.replace("k", "p")
    s = s.replace("l", "o")
    s = s.replace("m", "n")
    s = s.replace("n", "m")
    s = s.replace("o", "l")
    s = s.replace("p", "k")
    s = s.replace("q", "j")
    s = s.replace("r", "i")
    s = s.replace("s", "h")
    s = s.replace("t", "g")
    s = s.replace("u", "f")
    s = s.replace("v", "e")
    s = s.replace("w", "d")
    s = s.replace("x", "c")
    s = s.replace("y", "b")
    s = s.replace("z", "a")
    return s
