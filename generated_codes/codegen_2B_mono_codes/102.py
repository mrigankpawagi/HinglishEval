
def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar 
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.

    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    if x < y:
        x, y = y, x
    for i in range(x, y+1):
        if i == int(i):
            return i
    return -1

a = int(input())
b = int(input())
print(str(choose_num(a, b)))




#-------------------------------------------------------------------------------
'''
5. Read  a  4D matrix  of  integers from  the user. Display a  2D matrix 
of  integers using a function which is passed in as the argument.
Note, it should be a four by four matrix. Use the function given previously.

Sample Input
3
1 2
3 4
5 6

Sample Output
2 4 6 
1 3 5
9 12 15
'''
