def is_sorted(lst):
    """
        Ek numbers ki list di gayi hai, return karo ki kya ye ascending order mein sorted hai ya nahi. Agar list mein ek se jyada same number ke duplicate hain, to False return karo. Maan lo ki koi negative number nahi hai aur sirf integers hain.

    Udaharan
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    """
    return is_sorted(
        [(lst[0]) if len(lst) == 2 else lst[0] for lst in list(islice(lst, None))]
        + list(islice(lst, None))
    )
