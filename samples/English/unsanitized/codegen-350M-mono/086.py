
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello!!!Wdlor'
    """
    # return " ".join([f"{''.join(sorted(set(suc['name'] or''))).lower()}<{suc['location'] or ''}>" for suc in sorted(s)])

    suc = s
    # return " ".join([f"{''.join(sorted(set(suc['name'] or'')))}.{''.join(sorted(set(suc['location'] or''), reverse=True))}" for suc in sorted(s)])

    return " ".join([
        f"{''.join(sorted(set(suc['name'] or''))).lower()}<{''.join(suc['location'] or'').lower()}>"
        for suc in sorted(s)
    ]) + "\n"

print(anti_shuffle("Hi"))
print(anti_shuffle("Hello World!!!"))
print(anti_shuffle("Hello!!!Wdlor"))