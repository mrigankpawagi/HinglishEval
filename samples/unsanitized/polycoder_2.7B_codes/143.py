
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
    if sentence.strip().isalnum() or sentence in spaces:
        return "in"

    temp = ''

    original_sentence = sentence
    for c in sentence:
        if c in sentence[0].upper():
            # if we got a letter
            original_sentence = original_sentence.capitalize()
        elif c in temp:
            # if we got a word
            temp +=''

    temp =''.join(temp)
    # if we got more than one letter left that's a keyword word
    if temp.lower() in sentence[0].lower():
        temp ='' + temp
    elif temp:
        temp = '%s'% temp
    word