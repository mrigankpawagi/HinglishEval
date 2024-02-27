def solve(s):
    if any(c.isalpha() for c in s):
        return "".join(c.lower() if c.isupper() else c.upper() for c in s)
    else:
        return s[::-1]
