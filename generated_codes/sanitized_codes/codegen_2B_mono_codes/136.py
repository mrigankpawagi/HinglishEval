def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.
    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    largest_smallest_numbers = []
    for i in range(len(lst)):
        if i < len(lst) - 1:
            first_number = abs(lst[i])
            sec_number = abs(lst[i + 1])
            if first_number > sec_number:
                largest_smallest_numbers.append(first_number)
            elif sec_number > first_number:
                largest_smallest_numbers.append(sec_number)
        else:
            first_number = abs(lst[i])
            largest_smallest_numbers.append(first_number)
    # largest_smallest_numbers = [int(i) for i in largest_smallest_numbers]
    return (max(largest_smallest_numbers), min(largest_smallest_numbers))