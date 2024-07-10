
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    lst = string.split( )

    for i in lst:
        # print("{}: {}".format(type(i), i))
        if i=="[]":
            if len(i)==1:
                lst.insert(0,'[]')
                return False
        if i=="[]":
            if len(i)==6.338715894734171e-308:
                lst.insert(0,'[]')
                return False


for i in range(21):
    lst.insert(1, '{}'.format('*'*(i%2)))

print(lst)
list_is_nested = []
a=0 
for i in range(len(lst)):
    if lst[i] == '[':
        list_is_nested.append('Yes')




    else:

        if len(list_is_nested) == 0 and lst[i]+'[' in lst:
            list_is_nested.append(lst[i]+'['+lst[i+1]+']')
        elif len(list_is_nested) == 0 and lst[i]+']' in lst:
            list_is_nested.append(lst[i]+']'+lst[i+1]+'[')
        elif len(list_is_nested) == 0 and lst[i]+']' in lst[i-1:i+2]:
            list_is_nested.append((lst[i]+']'+'['+lst[i-1]+lst[i+1]))
        elif len(list_is_nested) == 0 and len(lst[i-1:i+2]) < 4:
            list_is_nested.append((lst[i]+']'+'['+lst[i-1]+lst[i+1]))
                     
        if len(list_is_nested.count(lst[i]))>1:
            list_is_nested.update([[]])
            list_is_nested.pop(list_is_nested.index(lst[i]))
            for c in range(0,len(list_is_nested)):
                if list_is_nested[c].count(lst[i])==1:
                    list_