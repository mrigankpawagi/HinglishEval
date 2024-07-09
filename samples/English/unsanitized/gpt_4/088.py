def sort_array(array):
    sorted_array = sorted(array)
    if (array[0] + array[-1]) % 2 == 0:
        return sorted_array[::-1]
    else:
        return sorted_array