
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # use binary search to get our answer
    # lst.append(end)
    answer=-1

    end=len(lst)
    answer=lst[0]
    while end > 1:
        mid=(end)//2
        if lst[mid]<answer:
            # print(answer)
            end=mid
            answer=lst[mid]
            # print(answer)
        else:
            # print(answer, mid)
            end=mid

    # we return the largest integer that is greater than 0
    # if the answer isn't -1, this is the only way i can think of
    # print("answer: %d, length:%d, mid: %d %d"%(answer,end,end/2,mid))
    return answer >= -1 and answer and lst[end] >= lst[end/2]


if __name__ == '__main__':
    l=range(7, 9)
    # x=range(6,10)
    maxF=0
    maxF_lst=[]
    maxF_lst.append(-1)

    while True:
        print(l)
        if maxF_lst[0] == -1:
            maxF_lst.append(x=search(l))
            if x == -1:
                break
        else:
            if maxF_lst> [-1]:
                # print("maxF", maxF,x,maxF==maxF_lst[0])
