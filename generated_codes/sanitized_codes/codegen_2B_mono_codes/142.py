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
    # code here
    if len(lst) <= 0:
        return 0
    i = 0
    sum = 0
    while i < len(lst) - 1:
        if type(lst[i]) != int:
            list_lst = list(set(lst))
            return -1
        sum += ((lst[i]) ** 2) * (3**i)
        i += 1
    return sum