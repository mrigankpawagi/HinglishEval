
def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.

    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    if len(lst) == 0:
        return (None, None)
    elif len(lst) == 1:
        return (None, lst[0])
    else:
        neg_lst = []
        pos_lst = []
        for i in lst:
            if i < 0:
                neg_lst.append(i)
            elif i > 0:
                pos_lst.append(i)
        if len(neg_lst) == 0:
            return (None, min(pos_lst))
        elif len(pos_lst) == 0:
            return (max(neg_lst), None)
        else:
            return (max(neg_lst), min(pos_lst))


# 2
def count_occurrences(lst, item):
    """
    Ek function banao jo ek list mein ek item ke occurrence ko count kare.

    Udaharan:
    count_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 1
    count_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 1
    count_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == 0
    """
    count = 0
    for i in lst:
        if i == item:
            count += 1
    return count


# 3
def count_occurrences_2(lst, item):
    """
    Ek function banao jo ek list mein ek item ke occurrence ko count kare.

    Udaharan:
    count_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 1
    count_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 1
    count_