
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
    if len(lst) == 0:
        return 0
    if len(lst) == 1: 
        return lst[0]


    odd_numbers = []
    result = 0
    for num in lst:
        if type(num) == int:
            print("in if 2: ", num, type(num))
            if num > 0:
                odd_numbers.append(num)
    print("in if 1: ", odd_numbers)
    for number in odd_numbers:
        result += number**2      

            

        

print(double_the_difference([1,3,2,0]))
print(double_the_difference([]))

#-----------------
# Question 2
import math


