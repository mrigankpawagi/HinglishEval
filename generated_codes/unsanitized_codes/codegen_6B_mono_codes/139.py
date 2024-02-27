
def special_factorial(n):
    """
    Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!
    jaha n > 0

    Jaise ki:
    >>> special_factorial(4)
    288

    Ye function ek integer input ke roop me lega aur is integer ka special
    factorial return karega.
    """
    if(n==0) or (n==1):
        return 1
    else:
        return n * special_factorial(n - 1)

if __name__=="__main__":
    import doctest
    doctest.testmod()


#######################################################################

"""
A man has n number of apples and he wishes to distribute them among several
people such that he wants each of them to eat exactly as much as possible as 
possible. So he has an array P (for each of the n people) of length n and, 
for each of the i'th element there is a value p (i-1) of the respective n number of apples 
(each of the apples is 1).
 Now you are given a list which is representing the distribution of apples among
 the n people. You need to distribute the apples amongst everyone such that no 
 person has more number of apples than his/her neighbour. And the program 
 should print out the number of groups which receive at least 1 apple each.

Input
The first line of the input contains T denoting the number of test cases. 
For each test case there will two lines. The first line contains n, representing
 the number of people in the group, and the second line contains n integers 
 representing the distribution of APPLES among the people.

Output
For each test case, you need to print the number of groups you want to get 
 at least 1 apple each, one line for each test case.

Constraints:
2 <= T <= 10
1 <= n <= 5000
0 <= P[i] <= 1000000000

Example
Input:
5
4
4 1 2 3
5
5 9 2 5
6
7 4 3 3
7
4 2 3 2

Output:
