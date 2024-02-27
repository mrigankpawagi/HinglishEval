def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in a fruit basket.
    Parameters:
    s (str): A string representing the number of apples and oranges in the fruit basket.
    n (int): The total number of fruits in the fruit basket.
    Returns:
    int: The number of mango fruits in the fruit basket.
    Examples:
    fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges", 120) -> 120 - 100 - 1 = 19
    """
    apples, oranges = map(int, s.split()[:2])
    return n - apples - oranges
