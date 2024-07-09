
def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.
    
    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    lst.sort()
    answer = sum(lst[1::2])
    return answer
lst = [5, 8, 7, 1]
print(solution(lst))

#############################################################################################################

#def solution(lst):
#   odds = []
#    x = 0
#    for i in range(len(lst)):
#        if lst[i]%2==1:
#            odds.append(lst[i])
#    for j in range(len(lst)-1):
#        if not j % 2:
#            k = j+1
#            if lst[j] % 2 == 0 and lst[k] % 2 == 1:
#               odds.append(max(lst[j],lst[k]))
#       elif j % 2:
#            if lst[j]%2==1:
#                odds.append(lst[j])
#   return sum(odds)
#
#print(solution([5, 8, 7, 1]))
# print(solution([30, 13, 24, 321]))
# print(solution([0, -21, -2, -4, -4, -5]))
# Output
#
# 24
# 0
# 0
#
########################################################################

# def solution(lst):
#   odds = []
#     x = 0
#    for i in range(len(lst)):
#        if lst[i]%2==1:
#            odds.append(lst[i])
#    for j in range(len(lst)-1):
#        if not j % 2:
#            k =