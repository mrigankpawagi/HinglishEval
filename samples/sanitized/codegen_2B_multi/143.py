
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
    """    # get len of the string
    # 1 <= str.count(' ') <= str.count('\n') <= 100
    length = len(sentence)

    # get all the letters in the string
    all_words = set(chars_in_sentence.findall(sentence))

    # set will have all the unique word
    result = []
    for word in all_words:
        # check whether word is a palindrome or not in the given word
        if word[::-1] in all_words:
            # if palindrome replace it with the string
            result.append(word)
        else:
            # else add to the result list the palindrome version
            new_word = word[::-1] + sentence[::-1]
            result.append(new_word)
    return "".join(result)
