
def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.
    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    lst.sort() # Ascending order
    if lst[0] == None:
        return (None, None)
    else:
        (max, min) = (lst[0], lst[0])
        for i in range(len(lst)):
            if lst[i] < 0:
                break
            elif lst[i] > max:
                max = lst[i]
            elif lst[i] < min:
                min = lst[i]
        return (max, min)