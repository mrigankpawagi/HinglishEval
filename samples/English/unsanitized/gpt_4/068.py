def pluck(arr):
    smallest_even = float('inf')
    smallest_index = -1
    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even:
            smallest_even = num
            smallest_index = i
    if smallest_index == -1:
        return []
    else:
        return [smallest_even, smallest_index]