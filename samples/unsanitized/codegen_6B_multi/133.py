

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
    sq_sum = 0
    for i in lst:
        sq_sum += i*i
    return int(round(sq_sum))

if __name__ == '__main__':
    # Test aad bn chh bhi huha, ki test chahiye ko.
    lst = [1,2,3,4,5,6,7]
    print sum_squares(lst)