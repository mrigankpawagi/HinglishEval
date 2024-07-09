
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    for numbers in range(1, len(nums)):
        current_sum = 0
        for i in str(nums[numbers]):
            current_sum += int(i)

        if current_sum > -10:
            print(nums[numbers])
            nums[numbers] = str(current_sum)
        elif current_sum < -1:
            print("Please sort the numbers in ascending order!")
            break


# test_nums = []
# while test_nums.__len__() < 5:
#     nums = input("Please enter some numbers: ").split()
#     test_nums = []
#     print("Test_nums: ", test_nums)
#     if len(nums) == len(set(nums)):
#         print("Your numbers are in a unique order")
#     else:
#         print("Please sort the numbers! ")
#         order_by_points(nums)
# count = 0
# for i in range(len(nums)):
#     if nums[i] % 1000 == 0:
#         count += 1
#     else:
#         print(str(nums[i]))
# print(str(count))

nums = [0]*1000
nums[0] = nums[0] + random.randint(0,999)
a = [(nums[i], i) for i in range(len(nums))]
print(a)
for i in range(5):
    print(i, end=' ')
    ans = list(a)
    count = 0
