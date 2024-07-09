
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
    input_string = 'is'
    output_string = 'go for'
    for i in range(-1, len(sentence)):
        if sentence[i] in input_string :
            sentence_num = 1
        else:
            sentence_num = None
        if sentence[i] == input_string :# if  i+1 < len(sentence) && sentence[i+1] == input_string: # if  i+2 < len(sentence) && sentence[i+1] == "then" sentence_num
            sentence_num = sentence[i+1]
        else:
            sentence_num = sentence[i]
    sentence = (sentence[0:1], sentence[1:])
    if sentence_num is not None :  #