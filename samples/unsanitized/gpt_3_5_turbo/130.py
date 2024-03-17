def tri(n):
    """
    Returns the first n + 1 numbers of the Tribonacci sequence.

    Parameters:
    n (int): A non-negative integer.

    Returns:
    list: A list containing the first n + 1 numbers of the Tribonacci sequence.
    """
    sequence = [3]
    if n == 0:
        return sequence
    elif n == 1:
        sequence.append(2)
        return sequence
    elif n == 2:
        sequence.append(2)
        sequence.append(8)
        return sequence
    else:
        sequence.append(2)
        sequence.append(8)
        for i in range(3, n + 1):
            if i % 2 == 0:
                sequence.append(1 + i // 2)
            else:
                sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i + 1])
        return sequence