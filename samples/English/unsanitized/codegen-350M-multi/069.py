
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # We create our list to store our integer values. This list keeps the sum of integers at the end.
    # If the integer does not exist in the list, the values are set as -1.
    lst_list = []

    # We search for the largest in reverse. It could be achieved by a simple bubble sort algorithm.
    for i in reversed(lst):
        if (min_val(i) < 0):
            lst_list.append(i)
            min_val(i)

    # If we've got a non-empty list, we return it.
    if lst_list and min_val(lst_list[0])!= -1:
        return min_val(lst_list)
    else:
        return -1

if __name__ == "__main__":
    tres = search([4, 1, 2, 2, 3, 1])
    print(tres, tres - 5)
