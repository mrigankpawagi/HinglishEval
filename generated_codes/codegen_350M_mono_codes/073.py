
def smallest_change(arr):
    """
    Ek array arr diya gaya hai integers ka, usme se minimum kitne elements ko change karna padega 
    taaki array palindromic ban jaye. Ek palindromic array woh hota hai jo aage se bhi aur peeche se bhi 
    same padhta hai. Ek change me, aap ek element ko kisi bhi dusre element se replace kar sakte ho.

    Jaise ki:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    arr.sort()
    answer = arr[-1] - arr[0]
    for x in range(1, len(arr)):
        answer = argsort(arr)
        for y in range(len(answer)):
            if answer[y] + arr[x] <= answer[y]:
                answer[y] += arr[x]

    p = 0
    for y in range(1, len(answer)):
        answer[p] = answer[p] - answer[y]
        p += 1

    return answer.count(0)


# print(f"smallest change({arr})")
# print(smallest_change([5, 8, 4, 3, 7, 2, 6, 1]))
# print(smallest_change([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# print(smallest_change([2, 3, 1, 2, 2, 4]))
# print(smallest_change([7, 2, 8, 5, 4, 3, 2, 1, 0]))


