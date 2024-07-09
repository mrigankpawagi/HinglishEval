
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
    even_numbers1 = [i for i in lst if i % 2 == 0]
    sums1 = 0
    for i in even_numbers1:
        sums1 += i * i
    totals = sum(even_numbers1) * 2
    
    odd_numbers2 = lst[:]
    sums2 = 0
    for i in odd_numbers2:
        sums2 += i * i
    totals += odd_numbers2[:] * 2
    total = sums1 + sums2 - totals + even_numbers1 + odd_numbers2
    
    return total
  
print (double_the_difference([]))

A:

There are a few problems. First of all, it's not clear on which Python version you're using, but at least in 3.x, there's an official name for this sort of construct: a generator expression. Try this:
total = sums1 + sums2 - totals + even_numbers1 + odd_numbers2

Note that Python will now be able to auto-indent the total line for you.
You may also want to look into the if __name__ == "__main__": block. From your code, it looks like you expect double_the_difference to be used as a global function, but at the moment it's just