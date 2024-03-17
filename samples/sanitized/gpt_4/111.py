def histogram(test):
    words = test.split()
    word_count = {word: words.count(word) for word in words}
    max_count = max(word_count.values(), default=0)
    return {word: count for word, count in word_count.items() if count == max_count}
