Here is the Python function that fulfills the requirements mentioned in the docstring:

```python
def words_in_sentence(sentence):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_words)
```

This function first defines a helper function `is_prime` to check if a number is prime. Then it splits the input sentence into words, filters out the words whose lengths are not prime numbers, and finally joins the remaining words back into a sentence.