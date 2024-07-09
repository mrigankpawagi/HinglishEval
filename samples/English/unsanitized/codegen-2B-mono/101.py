
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    sentence_words = s.split(', ')

    for i in range(0, len(sentence_words)):
        sentence_words[i] = sentence_words[i].strip()
        sentence_words[i] = sentence_words[i].lower()

    return list(filter(None, sentence_words))


words = ["Hi",
 "my",
  "name",
  "is",
  "John",
 ]

# [word for word in "Word, word" if ]
print(words_string(words))
