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
    a = lst[0]
    i = 0
    output = 0
    for j in lst:
        if j % 3 == 0:
            try:
                if lst[i + 3] % 3 == 0:
                    a = (a + j) ** 2
                    i += 1
            except IndexError:
                a += j
                i += 1
            if a > output:
                output = a
        elif j % 4 == 0:
            try:
                if lst[i + 4] % 4 == 0:
                    a = (a + j) ** 3
                    i += 1
            except IndexError:
                a += j
                i += 1
            if a > output:
                output = a
    return output