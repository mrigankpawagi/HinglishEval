
def is_nested(string):
    """
    Ek function banao jo sirf square brackets wala string input ke roop mein leta hai.
    Function tabhi True return karega jab valid subsequence of brackets ho 
    jisme kam se kam ek bracket nested ho.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    """
    string = str(string)

    substrings = list(set(string))

    if any(substring == []) or any(substring == []) or any(substring == []):
        return True
    if [substring for substring in substrings if is_nested(substring)]:
        return True
    if all(substring == [] for substring in substrings):
        return False
    return all(substring == 0 for substring in substrings)
