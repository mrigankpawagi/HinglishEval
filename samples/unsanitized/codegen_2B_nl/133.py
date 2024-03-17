

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
    total = 0
    i = len(lst) - 1
    while i >= -2:
        total = total + (abs(lst[i] - lst[i-1]) ** 2)
        i = i - 1
    return total

if __name__== '__main__':
    print(sum_squares([-5e5,2]))
    print(sum_squares([4,-2,3]))
    print(sum_squares([1,1,2]))
    print(sum_squares([3,-4,-8]))

Note: The function returns the value as a float (you can change it back to an integer by changing return float(ceil(total/Ceiling())) to return int(ceil(total/Ceiling())). 

