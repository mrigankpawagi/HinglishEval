def select_words(s, n):
    vowels = 'aeiouAEIOU'
    words = s.split()
    result = []
    for word in words:
        count = 0
        for letter in word:
            if letter not in vowels:
                count += 1
        if count == n:
            result.append(word)
    return result