


def sum_squares(lst):
    """
    "
    Ye function ek integers ki list lega. List ke saare entries ke liye, function integer entry ko square karega agar uska index 3 ka 
    multiple hai aur cube karega agar uska index 4 ka multiple hai aur 3 ka multiple nahi hai. Function un entries ko change nahi 
    karega jinki indexes 3 ya 4 ka multiple nahi hai. Phir function saare entries ka sum return karega. 
    
    Examples:
    Agar lst = [1,2,3] hai to output 6 hona chahiye
    Agar lst = []  hai to output 0 hona chahiye
    Agar lst = [-1,-5,2,-1,-5]  hai to output -126 hona chahiye
    """
    k=[]
    list_lst = []
    for i in lst:
        k.append(i)
    for karr in k:
        list_lst.append(karr*karr)
    list_len = len(list_lst)
    pz = 0
    n = 0
    sum_lst = 0
    while n < list_len:
        pz=n
        sum_lst=sum_lst+list_lst[pz]
        n = n+1
    if list_lst == sum_lst:
        print "Yes"
    elif sum_lst > sum_lst:
    # If sum_lst is bigger than sum_lst then, result must be 'No' else it must be "Yes"
        print "No"
    else:
        print "Yes"

'''
lst = []
lst = [7,-7]
print sum_squares(lst)
'''

