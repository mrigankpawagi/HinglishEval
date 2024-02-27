def split_words(txt):
    """
    Ek string di gayi hai jisme words hain, aapko ek list return karni hai jisme words whitespace par split ho. Agar text me koi whitespace nahi hai toh aapko commas ',' par split karna hai. Agar koi comma bhi nahi hai toh aapko alphabet me odd order wale lower-case letters ki count return karni hai, jaise ki ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Udaharan
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    """
    nb = 0
    for line in open(FILE_NAME):
        # line.split() runs in a for loop until we come upon an empty line and it splits
        for line_str_ in line.split():
            nb = nb + 1 + line_str.split()
        # We add the first line to the beginning, then the rest, then the first
        # and second lines, so that we have a line that is the same as the first two
        for s in split_str_split(line_str):
            nb += 1
    return split_words(txt)