

def skjkasdkd(lst):
    """
    Aapko ek list di gayi hai integers ki.
    Aapko sabse bada prime value dhundna hai aur uske digits ka sum return karna hai.

    Udaharan:
    Agar lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] hai to output hona chahiye 10
    Agar lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] hai to output hona chahiye 25
    Agar lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] hai to output hona chahiye 13
    Agar lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] hai to output hona chahiye 11
    Agar lst = [0,81,12,3,1,21] hai to output hona chahiye 3
    Agar lst = [0,8,1,2,1,7] hai to output hona chahiye 7
    """


    lst_sum = 0
    lst_primes = []
    for i in lst:
        if i > 1:
            for j in range(2, i + 1):
                if not i%j:
                    lst_sum += i
                    break
        lst_primes.append(lst_sum)
    return max(lst_primes)


a = [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 223, 32, 324, 4, 3]
print(skjkasdkd(a))
print(skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]))
print(skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]))
print(skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]))
print(skjkasdkd([0, 81, 12, 3, 1, 21]))
print(skjkasdkd([0, 8, 1, 2, 1, 7]))
