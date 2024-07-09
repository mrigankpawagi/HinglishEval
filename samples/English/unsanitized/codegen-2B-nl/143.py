
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    new_string = ""
    max_len = max([len(w) for w in sentence])
    if len(sentence) == 1:
        return sentence[0]
    for i in range(1, len(sentence)):
        for j in range(i):
            if len(sentence[i]) < len(sentence[j]):
                return "", 0
            if len(sentence[i]) == len(sentence[j]):
                word_length = len(sentence[j])
            if new_string:
                new_string +=''
            new_string += sentence[i]
            new_string += word_length
            if new_string:
        