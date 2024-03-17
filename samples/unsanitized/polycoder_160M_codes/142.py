


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
    #
    # def sum_squares(lst):
    #     if not isinstance(lst, list): lst = [lst]
    #
    #     total_squares = 0
    #     for v in lst:
    #         for j in v:
    #             i = 0
    #             j = int(j & 1) % 100
    #             if i == j and j == total_squares < total_squares:
    #                 total_squares += 10
    #             else: i += 50
    #     return total_squares / 50
    #

    lst_list=lst.split()
    for lst_1 in lst["list"]:
        i = 0
    