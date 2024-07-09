def compare(game, guess):
    return [abs(a-b) for a, b in zip(game, guess)]