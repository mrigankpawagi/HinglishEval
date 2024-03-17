def select_words(s, n):
    vowels = "aeiouAEIOU"
    words = s.split()
    return [
        word for word in words if sum(1 for char in word if char not in vowels) == n
    ]
