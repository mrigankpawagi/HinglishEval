
def split_words(txt):
    """
    Ek string di gayi hai jisme words hain, aapko ek list return karni hai jisme words whitespace par split ho. Agar text me koi whitespace nahi hai toh aapko commas ',' par split karna hai. Agar koi comma bhi nahi hai toh aapko alphabet me odd order wale lower-case letters ki count return karni hai, jaise ki ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Udaharan
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    """
    return txt.split()
