
def split_words(txt):
    """
    Ek string di gayi hai jisme words hain, aapko ek list return karni hai jisme words whitespace par split ho. Agar text me koi whitespace nahi hai toh aapko commas ',' par split karna hai. Agar koi comma bhi nahi hai toh aapko alphabet me odd order wale lower-case letters ki count return karni hai, jaise ki ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Udaharan
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    """
    karnim_lines = ""
    whole_words = []
    wanted_words = list()
    for word in txt.split(','):
        wanted_words.append(word)
    replaced = []
    for w in wanted_words:
        replaced.append(w.replace('(', '').replace(')', '').replace(whole_words, ''))
    return karnim_lines, replaced, whole_words
