
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
    if sentence is None:
        return None
    sent_copy = sentence.copy() 
    sent_copy = sent_copy.replace(" ", "")
    if not sent_copy:
        return None
    sentence_len = len(sent_copy)
    for i in range(1, sentence_len):
        if " " not in sent_copy and "," not in sent_copy and "." not in sent_copy and ";" not in sent_copy and "!" not in sent_copy and "!" in sent_copy:
            sent_copy = ""
        sent_copy = sent_copy.split(" ")
        sent_copy = list(map(lambda x: x.strip().lower(), sent_copy))
        for kata in sent_copy:
            if kata and not kata[0].isalpha():
                # print(kata)
                if not kata[len(kata) - 1] == ".":
                    return "no"
            else:
                for letter in kata:
                    # print(str(letter) + str(letter[0]))
                    if not letter[0].isalpha():
                        return "no"
                    else:
                        if kata.count('.') > 1:
                            if sentence_len == kata.count('.'):