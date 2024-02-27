def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.split(",")
    else:
        return sum(1 for c in txt if ord(c.lower()) % 2 == 1)
