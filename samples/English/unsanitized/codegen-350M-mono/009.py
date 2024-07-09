from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers_length = len(numbers)

    # create a new sequence of numbers
    numbers_as_sequence = []
    index = 0
    while numbers_as_sequence == []:
        # if a new number is calculated at the end
        if index == numbers_length:
            numbers_as_sequence[-1] = numbers[index]
            break
        # check if a maximum exists at the given moment (i.e. not out of limit and it is the largest number
        # in the sequence)
        if numbers[index] > numbers[index + 1]:
            maximum = numbers[index]
            numbers_as_sequence.append(maximum)
            # for all the positions in sequence, increment the element to move to current position, or if we have finished calculating them.
            for i in range(index, numbers_length):
                numbers_as_sequence[-1] = numbers_as_sequence[-1] + numbers[i]
            # if after going through all positions
            if i == numbers_length - 1:
                break
            # if we don't want to calculate the next number
            numbers_as_sequence[-1] -= numbers[index + 1]
            index += 1
        # if a greater maximum at the end of sequence then it is the last number
        elif numbers[index] > numbers[index + 1]:
            numbers_as_sequence[-1] = numbers[index]
            index += 1
        # if the current element is the largest of the sequence, then append that it to the list
        elif numbers[index] == numbers[index + 1]:
            numbers_as_sequence.append(numbers[index])
            index += 1

        # if the current element is the last of the sequence
        elif numbers[index