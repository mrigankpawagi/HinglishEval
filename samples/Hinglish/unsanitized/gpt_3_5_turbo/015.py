def string_sequence(n: int) -> str:
    """
    Returns a string containing numbers from 0 to n, separated by spaces.
    """
    return ' '.join(str(i) for i in range(n+1))