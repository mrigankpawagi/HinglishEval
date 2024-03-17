def vowels_count(s):
    """
    Returns the count of vowels in a given string.
    Parameters:
    s (str): The input string.
    Returns:
    int: The count of vowels in the string.
    """
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count
