
def split_words(txt):
    """
    Ek string di gayi hai jisme words hain, aapko ek list return karni hai jisme words whitespace par split ho. Agar text me koi whitespace nahi hai toh aapko commas ',' par split karna hai. Agar koi comma bhi nahi hai toh aapko alphabet me odd order wale lower-case letters ki count return karni hai, jaise ki ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Udaharan
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    """
    result = []
  
    i = 0
    
    while i < len(txt):
        check = txt[i]
        if txt[i] == " " or txt[i] == ",":
            x = 0
            sub_txt = txt[i+1:]
            while x < len(sub_txt):
                if sub_txt[x] == " " or sub_txt[x] == ",":
                    pass
                else:
                    break
                x += 1
            result.append(txt[i+1:x+1])
        elif txt[i] == '.':
            result.append(txt)
            break
        i += 1
    return sorted(result, key=lambda x: len(x), reverse=True)
