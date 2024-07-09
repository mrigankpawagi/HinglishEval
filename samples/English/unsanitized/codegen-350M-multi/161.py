
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    if not is_valid_input(s):
        if s == '':
            return ''
        else:
            raise ValueError("Invalid input character.")
    # Remove consecutive spaces
    str = re.sub(r',+', '', s)
    str = re.sub(r'(.)', r'\1', str)
    # Split on the delimiter
    chunks = split_words(str, " ")
    result = chunks[0]
    start = 1
    for i, c in enumerate(str):
        if c in '0123456789':
            result = result + c
            if s.count(result)!= 1:
                chunks.pop(i)
                start += 1
    # Check if there are no spaces
    if(chunks[0] == ''):
        chunks.pop(0)
    # Return the result
    return chunkify(chunks)

if __name__ == '__main__':
    print(solve("1234"))
    print(solve("#a@C"))
