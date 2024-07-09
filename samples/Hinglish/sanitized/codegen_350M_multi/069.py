def search(lst):
    """
    Aapko ek non-empty list di gayi hai positive integers ki. Return karo sabse bada integer jo zero se bada ho,
    aur uska frequency us integer ke value ke barabar ya usse zyada ho.
    Ek integer ka frequency uski list mein kitni baar aane ki sankhya hoti hai.
    Agar aisa koi value nahi hai, to -1 return karo.
    Udaharan:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    """
    poslist = sorted(lst)
    return int(-poslist[0]) if len(lst) > 0 else 0