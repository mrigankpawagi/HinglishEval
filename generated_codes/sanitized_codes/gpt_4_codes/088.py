def sort_array(array):
    if not array:
        return array
    else:
        sum_of_first_and_last = array[0] + array[-1]
        if sum_of_first_and_last % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)
