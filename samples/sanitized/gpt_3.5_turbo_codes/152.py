def compare(scores, guesses):
    return [
        0 if score == guess else abs(score - guess)
        for score, guess in zip(scores, guesses)
    ]
