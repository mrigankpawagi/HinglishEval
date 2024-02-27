def find_max(words):
    max_unique_chars = max(words, key=lambda x: len(set(x)))
    max_unique_chars_list = [
        word for word in words if len(set(word)) == len(set(max_unique_chars))
    ]
    return min(max_unique_chars_list)
