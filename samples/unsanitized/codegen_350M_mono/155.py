
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_odd_count_ = dict()
    if num < 0:
        while (num!= 0):
            num = num//10
            if num % 2==0:
                even_odd_count_[num]=1
            else:
                even_odd_count_[num]=2
        return even_odd_count_
    elif num%2==0:
        return even_odd_count_
    else: 
        return even_odd_count_

#def even_odd_count_2(num, count):
#    """
#    Tuple diya gaya hai karo nahi gaya hai
#    Udaharan:
#        even_odd_count_2(-12) ==> (1, 0)
#        even_odd_count_2(123) ==> (1, 1)
#    """
#    even_odd_count_ = tuple()
#    if num < 0:
#        while num!= 0:
#            num = num//10
#            if num % 2==0:
#                even_odd_count_+=str(num)
#            else:
#                even_odd_count_+=str(num)
#        count+=1
#        return even_odd_count_, count
#    elif num%2==0:
#        even_odd_count=tuple()
#        count+=1
#        return even_odd_count,count
#    else:
#        return even_odd_count

