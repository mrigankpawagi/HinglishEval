
def will_it_fly(q,w):
    """
    Ek function likho jo True return kare agar object q udega, aur False otherwise.
    Object q tabhi udega jab vo balanced ho (yani ki ek palindromic list ho) aur uske elements ka sum maximum possible weight w se kam ya barabar ho.

    Udaharan:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 maximum possible weight se kam hai, lekin ye balanced nahi hai.

    will_it_fly([3, 2, 3], 1) ➞ False
    # ye balanced hai, lekin 3+2+3 maximum possible weight se jyada hai.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 maximum possible weight se kam hai, aur ye balanced hai.

    will_it_fly([3], 5) ➞ True
    # 3 maximum possible weight se kam hai, aur ye balanced hai.
    """
    if q == [] and w == 0:
        return True
    else:
        if len(q) ==0 and w != 0:
            return False
        elif len(q) > 0 and w >= sum(q):
            if len(q) == 1:
                return True
            else:
                return q[-1] +  sum(q[:-1]:2) == w 
        elif len(q) > 0 and w < sum(q):
            return False
    # for i in range(len(q)):
    #     if q[0] == q[-1]:
    #         del(q[0])
    #         del(q[len(q) -1])
        return will_it_fly(q[2:-2],w-sum(q[-2:-1])]
    
    



"""
N
Write function add_two_lists, which will add two lists of numbers element-wise.
Your function should return a new list with all the elements in the result.


Examples:

add_two_lists([3, 6, 2], [8, 1]) ➞ [11, 7, 2]
add_two_lists([1, 1, 1], [5, 5, 5]) ➞ [6, 6, 6]
add_two_lists([1, 2, 3], [4, 5]) ➞ [5, 7, 3]

"""


def add_plus_two_lists(lst1,lst2):
    return [sum(i) for i in zip(lst1, lst2)]


print(add_plus_two_lists([3, 6, 2], [8, 1]))



"""
Write a function will_it_fly(q, w) in Python(with the main() template below) that returns True if the object q will fly and False otherwise. 
The object q will only fly if it is balanced (i.e., a palindromic list) and if the sum of the elements is smaller or equal to maximum possible weight w. 
The weight w of a list means the sum of all of its elements.

Example:will_it_fly([1, 2], 