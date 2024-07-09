
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
    tup = [int(lst[k]) for k in range(lst.size)]
    fprintf(fp,'%i\n',str.lowercase(tup[-1]))

    for i in range(0,lst.size) with i < lst.size-1:
        fprintf('%i\n',str.lowercase(tup[i]))
        fprintf('%i\n',str.lowercase(tup[i+1]))

    return search(tup)

if __name__ == "__main__":
    input = input()
    for l in range(20):
        int_search = search(input)
        printf('%i\n',int_search)

# Output
0
1
2
3
4
4
4
4
4
4
5
5
5
5
5
5
5

A:

My favorite function to write lists of size N is the one from the Python coreutils.
list_elements_of()
