
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

if __name__ == '__main__':
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) # Result : (1, 7)
    print(largest_smallest_integers([0])) # Result : (None, None)
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7, 0])) # Result : (1, 7)
    print(largest_smallest_integers([2, 1, 4])) # Result : (None, 8)
    print(largest_smallest_integers([])) # Result : (None, None)
    print(largest_smallest_integers([3, 4])) # Result : (None, 3)
    print(largest_smallest_integers([3, 0, 4])) # Result : (None, 4)
    print(largest_