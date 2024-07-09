
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
    import math

    # Get all of the words in the sentence
    words = sentence.split()

    # Use a set of prime numbers so that if there are words with the same length they are all counted at the end
    prime_numbers = set(prime for prime in range(4, 100) if not any(math.isprime(prime) for word in words if len(word) == prime))
    prime_numbers.remove(len(words[0]))

    # Only words are allowed
    prime_numbers = max(prime_numbers, key=lambda x: len(words))

    # Convert to an iterator
    prime_numbers = iter(sorted(prime_numbers))
    word_lengths = []
    while words:
        word_lengths.append(len(words.pop()))

    # Create a list of numbers from the prime numbers
    words_to_get = []
    number = 0
    while word_lengths:
        length = word_lengths.pop()
        for _ in range(prime_numbers - number):
            words_to_get.append(next(prime_numbers))
        number = words_to_get[-1]
    if words_to_get:
        words_to_get.reverse()

    return ''.join(words_to_get)


