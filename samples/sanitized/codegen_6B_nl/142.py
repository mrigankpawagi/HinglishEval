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
    for i in lst:
        if i % 2 == 1:
            continue  # Even number only
        elif i % 3 == 0:  # Number divisible by 3 only
            continue
        elif i % 4 == 0:  # number divisible by 4 only
            continue
        else:
            print(i)