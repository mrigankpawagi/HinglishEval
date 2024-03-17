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
    # Input and Output
    # sentence = "This is a test"
    # Code
    cnt = 0
    for i in sentence.split():
        if i not in string.ascii_letters:
            continue
        else:  # This is a great place to check if the last bit is a vowel or not.
            length = 0
            while i != "":
                cnt += 1
                if i[length] not in string.ascii_letters:
                    pass  # This is the good part.
                else:
                    return
                length += 1
        if i.isnumeric() == True:
            # If it's a number, check the last one.
            length = 0
            while i != "":
                cnt += 1
                if i[length] not in string.ascii_letters:
                    pass
                elif not i[length].isnumeric():
                    # This is the good part.
                    break
                length += 1