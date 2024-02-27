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
    sentence = sentence.strip().split(" ")
    return set(sentence[0 : len(sentence) // 2]) == set(sentence[1 : len(sentence)])