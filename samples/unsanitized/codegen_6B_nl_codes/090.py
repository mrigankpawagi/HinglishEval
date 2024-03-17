
def next_smallest(lst):
    """
    Aapko ek list di gayi hai integers ki.
    Ek function likho next_smallest() jo list ka 2nd sabse chhota element return kare.
    Agar aisa koi element nahi hai to None return kare.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    
    if lst == []:
        return None
    else:
        for ii in lst:
            if ii < lst[-1] :
                lst[-2], lst[-1] = lst[-1], lst[-2] # 1st change the size of array
                lst.pop() # remove the element that gets pushed to the back
                print ('sai to chota element {}'.format(lst)) # output the size
                lst[1], lst[0] = lst[0], lst[1] # 2nd change the size of array
        print ('{} element lst size: {}'.format(lst[-1], len(lst)))
    return lst[0]
    
# driver to test next_smallest

list_to_test = [1, 2, 5, 1, 4, 2]
print ('First array element: ', list_to_test[0])
output = list_to_test[:]
print ('New array with 1 element after next_smallest(): ', 
    