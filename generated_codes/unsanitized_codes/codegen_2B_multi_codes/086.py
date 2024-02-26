
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello!!!Wdlor'
    """
    def print_message(_str) :
        print(_str)
    def get_tokens(_str) :
        tokens = _str.strip().split(" ")
        for element in tokens:
            tokens.remove(element)
        tokens.sort(key=lambda word: ord(word))
        return [word for word in tokens]
    def make_ascii_table(_message) :
        ascii = {}
        message = get_tokens(_message)
        for index in range(0,len(message)):
            ascii[index] = chr(ord(' A') - ord(message[index]) + 1)
        return ascii
    def anti_shuffle2(_message, _index) :
        ascii_table = make_ascii_table(_message)
        tokens = get_tokens(_message)
        return tokens[:_index] + [ascii_table[index] + token for index, token in enumerate(tokens[_index:])] + tokens[_index:]
    def anti_shuffle3(_message, _index) :
        tokens = get_tokens(_message)
        return tokens[:_index] + [tokens[(_index - 1) % len(tokens)], tokens[(_index + 1) % len(tokens)]] + tokens[_index:]
    def anti_shuffle4(_message, _index) :
        tokens = get_tokens(_message)