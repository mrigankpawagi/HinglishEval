
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
    prime_list = primes_or_modulus()
    new_sentence = ''
    i = 0

    while i < len(sentence):
        char = sentence[i]

        if char not in (' ', '.', ':') and char.isalpha():
            if char in prime_list:
                tmp_word = ''

                while i < len(sentence) and sentence[i] in prime_list:
                    tmp_word += sentence[i]
                    i += 1

                num_of_primes = int(len(prime_list) / prime_list.index(tmp_word) - 1)

                if num_of_primes == 1:
                    new_sentence += tmp_word +''
                elif num_of_primes > 1:
                    new_sentence += tmp_word[1:] +''
                    for j in range(2, num_of_primes + 1):
                        new_sentence += prime_list[prime_list.index(tmp_word) * j]

            else:
                new_sentence += char

        i += 1

    return new_sentence


# Tests
