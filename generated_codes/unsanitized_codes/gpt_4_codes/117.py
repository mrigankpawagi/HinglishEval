Here is the Python function that fulfills the requirements:

```python
def select_words(s, n):
    vowels = 'aeiouAEIOU'
    words = s.split()
    return [word for word in words if sum(1 for char in word if char not in vowels) == n]
```
This function first splits the input string into words. Then it uses a list comprehension to select the words that have exactly n consonants. The number of consonants in a word is calculated by summing 1 for each character in the word that is not a vowel.