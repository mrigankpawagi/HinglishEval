

def sum_squares(lst):
    """
    Aapko ek numbers ki list di gayi hai.
    Aapko di gayi list ke squared numbers ka sum return karna hai,
    pehle har element ko list mein upper int(Ceiling) par round karo.
    Udaharan:
    Agar lst = [1,2,3] hai to output hona chahiye 14
    Agar lst = [1,4,9] hai to output hona chahiye 98
    Agar lst = [1,3,5,7] hai to output hona chahiye 84
    Agar lst = [1.4,4.2,0] hai to output hona chahiye 29
    Agar lst = [-2.4,1,1] hai to output hona chahiye 6
    """
    print(lst)
    total = 0
    for num in lst:
        total += (num)**2;
    return (total)
    #code here


# Test your function with the following test cases:
print("Pass" if (2 == sum_squares([1, 2, 3])) else "Fail")
print("Pass" if (30 == (sum_squares([1, 2, 3]))) else "Fail")
print("Pass" if (6 == (sum_squares([1.3, 2.7, 1.1, 3.4, 4.1]))) else "Fail")

print("Pass" if ((28 == sum_squares([ 4, 25, 26, 29, 33, 49 ]))) else "Fail")
print("Pass" if ((3788 == sum_squares([1.4, 5.2, 4.5, 5.1, 0.4, 5 ]))) else "Fail")

