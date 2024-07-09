
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even = 0
    odd = len(lst) - 1
    while even <= odd:
        if even == 0:
            even, even = even + 1, lst[odd]
            continue
        if odd == len(lst):
            odd -= 1
            continue
        if lst[even] % 2 == 0:
            lst[odd] = lst[even] + lst[even + 1]

        if lst[even] % 2:
            lst[odd] = lst[even] + lst[even - 1]

        if lst[even] % 2 == 1:
            lst = lst[:even] + [lst[even] + lst[odd]] + lst[odd + 1:]

        if lst < 0:
            left_to_left = lst[:len(lst) - 1]
            left_to_right = lst[-1:]

        for right_to_right in range(odd, -1, -1): 
            if lst < 0:
                left_to_left.pop()
                left_to_right = 0
                break
            if lst[right_to_right] % 2 == 1:
                lst = lst[:right_to_right] + [lst[right_to_right] + lst[(right_to_right-1)]] + [lst[right_to_right]] - lst
                break
        for right_to_left in range(odd+1, len(lst)): 
            if lst < 0:
                left_to_right = 0
                break
            if lst[right_to_left] % 2 == 1:
                lst = lst[:right_to_left] + [lst[right_to_left] + lst[left_to_left]] + [lst[left_to_left]] + lst[left_to_