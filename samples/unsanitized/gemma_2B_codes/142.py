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
    sum = 0
    for i in lst:
        if i % 3 == 0 and i % 4 == 0:
            sum += i**2
        elif i % 3 == 0:
            sum += i**3
        else:
            sum += i
    return sum


print(sum_squares([1, 2, 3]))
print(sum_squares([]))
print(sum_squares([-1, -5, 2, -1, -5]))
