def split_words(txt):
    """
    Ek string di gayi hai jisme words hain, aapko ek list return karni hai jisme words whitespace par split ho. Agar text me koi whitespace nahi hai toh aapko commas ',' par split karna hai. Agar koi comma bhi nahi hai toh aapko alphabet me odd order wale lower-case letters ki count return karni hai, jaise ki ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Udaharan
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    """
    result = []
    # split on whitespace and return result as list
    for index, letter in enumerate(txt):
        # split on comma
        _, result_tmp = txt.split(",")
        result.append(result_tmp)
        # remove whitespace from list
        result = [
            (
                letter
                if is_whitespace(letter)
                else letter.lower() if letter.islower() else letters.upper()
            )
            for letter in result
        ]
        # return the last word if it does not have a lowercase letter or is all whitespace or alphabet
        if len(result) < index + 1 or is_alphabet(result):
            result.pop()
    return result