

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
    """
    aamal ke sum_squares(lst) method hai.
    """
    lst.sort()
    # print(lst)
    sum = 0
    for i in lst:
        sum=sum+i*i
    sum_squared=round(sum)
    return sum_squared

lst = [1,2,3] # lst = [1,2,3]
print(sum_squares(lst))#to get hai hai print output 91;
lst.append(10) # lst =[1,2,3,10 ]
print(sum_squares(lst))#to get hai hai print output 106;
lst.insert(1,-1) # lst = [],1 insertion for [-1,2,3]
print(sum_squares(lst))#to get hai hai print output 106;
lst.append(-1) # lst =[-1] insertion for [-1,2,3]
print(sum_squares(lst))#to get hai hai print output 106;
lst.append(-1) # lst =[-1,5] insertion for [-1,2,3,5]
print(sum_squares(lst