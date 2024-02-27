

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
    # list ke upper int() aur round karne ka hai
    # upper int(Ceiling) par round ki ne
    #   
    # Upper (rounded up): Ceiling - 1
    sum_1 = 0
    lower_int = 0
    while lower_int < len(lst):
        lower_int += 1
        sum_1 += lst[lower_int-1]
        for i in range(lower_int, len(lst)):
            if i == lower_int:
                lower_int += 1
    # round ke sum sum_1
    sum_elements = round(sum_1, -1)
    # print(sum_elements)
    total = sum_elements
    total_list = []
    for i in range(lower_int, len(lst)):
        total_list.append(lst