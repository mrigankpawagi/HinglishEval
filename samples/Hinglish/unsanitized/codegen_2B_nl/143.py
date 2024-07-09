
def words_in_sentence(sentence):
    """
    Aapko ek string di gayi hai jo ek sentence ko represent karti hai,
    sentence mein kuch words hote hain jo space se separate hote hain,
    aur aapko ek string return karni hai jo original sentence ke words ko contain karti hai,
    jinki lengths prime numbers hain,
    nayi string mein words ka order original wale ke jaisa hi hona chahiye.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence sirf letters contain karti hai
    """
    words_in = []
    string_length = len(sentence) - 1
    i = 0
    while i <= string_length:
        i += 1
        if sentence[i].isascii():
            words_in.append(sentence[i])
        else:
            word_i = sentence[i].lower()
            if word_i in words_in:
                word_i += " " * (string_length - (i - i_start))
            else:
                word_i = word_i + " " * (string_length - (i - i_start))

        i_start += 1

 