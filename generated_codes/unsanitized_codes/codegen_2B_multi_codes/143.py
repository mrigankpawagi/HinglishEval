
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
    result = ''
    str_lengths = []

    for char in sentence:
        str_lengths.append(len(string))
        if len(result) < max(str_lengths):
            result += char
    str_lengths = []
    for char in sentence:
        str_lengths.append(len(result))

    max_len = max(str_lengths)

    for i in range(0, max_len + 1):
        word = list(filter(lambda x: i < x, str_lengths))

        if word:
            for j in word:
                result2 = ''
                for k in range(i):
                    if k < j:
                        result2 +=''
                    result2 += char
                result += result2
                
                result2 = ''
                for n in range(j+1):
                    if n < i:
                        result2 +=''
                    result2 += char
                result += result2
                break
    return result

if __name__ == '__main__':
    _print(words_in_sentence('the night is full of darkness!'))