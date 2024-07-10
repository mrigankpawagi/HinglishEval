
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    # your code here
    lst1 = lst1.sort()
    lst2 = lst2.sort()
    print(lst1, lst2)
    if len(set(lst1)) == len(set(lst2)):
        return lst2
    elif len(set(lst1)) < len(set(lst2)):
        a = sorted(lst2)
        return a
    else:
        a = lst1
        return a
#         print(sorted_lst[0].lower() + sorted_lst[1].lower())
#         count_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
#         if s1 in count_dict.keys():
#         count_dict[s1]+=1
#          if s2 in count_dict.keys():
#               count_dict[s2]+=1
#          if count_dict[s1]<count_dict[s2]:
#               print(s1, s2)
#          return s1
#          return s2
# for s in sorted_lst:
#      print(s)
#     

# if __name__ == '__main__':
#     assert total_match([], []) == [], 'Failed 1'
#     assert total_match([], ['1', '2', '3']) == [], 'Failed 2'
#     assert total_match(['admin', 'admin', 'admin'], ['hi', 'admin', 'hi']) == ['admin'], 'Failed 3'
#     assert total_match(['foo', 'bar', 'foobar', 'barfoo', 'foo'], ['fo', 'bar', 'f', 'foobar', 'foobarbaz']) == ['barfoo', 'foo'], 'Failed 4'
