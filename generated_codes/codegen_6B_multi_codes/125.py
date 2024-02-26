
def split_words(txt):
    """
    Ek string di gayi hai jisme words hain, aapko ek list return karni hai jisme words whitespace par split ho. Agar text me koi whitespace nahi hai toh aapko commas ',' par split karna hai. Agar koi comma bhi nahi hai toh aapko alphabet me odd order wale lower-case letters ki count return karni hai, jaise ki ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Udaharan
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    """
    def get_letters_count(letters):
        count = 0
        for letter in letters:
            count += ord(letter) - ord('a')
        return count
    def generate_word(text, split):
        '''
        text string ke words jisme ke words hai, odd number par split ke words hai
        '''
        start, end = 0, split-1
        while start < len(text):
            if get_letters_count(text[start:end]) % 2 == 1:
                return text[start:end]
            start, end = start+1, end-1
        return ''
    result = []
    text = txt.lower()
    for s in''*split:
        words = generate_word(text, split+len(s))
        if words:
            result.append(words)
        if len(text) == split+1:
            return result
    return result


