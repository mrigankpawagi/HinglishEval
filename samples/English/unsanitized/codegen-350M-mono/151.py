
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    for number in lst:
        if number < 0:
            return 0
    return (sum([i**2 for i in lst if i % 2!= 0]) ** 2)

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('lst: [9, 10, 1, 9, 2], Output : 18')
    print('Exception :')
    print('18')
    print()

    try:
        print('Example 2:')
        print('Input : ')
        print('lst: [9, 4, 6, 10, 8, 3, 20, 10], Output : 91')
        print('Exception :')
        print('91')
        print()

        print('Example 3:')
        print('Input : ')
        print('lst: -9, 0, 8, -10, 0, 8, -10, -6, 9, -6, 9, 4, -6, -9, 0, 4')
        print('Exception :')
        print('0')
        print()

        print('Example 4:')

        print('Input : ')
        print('lst: 2, 2, 5, 3, 3')
        print('Exception :')
        print('4')
        print()

        print('Example 5:')
        print('Input : ')
        print('lst: 4, 8, -6, 13, 9, 7, -8')
        print('Exception :')

