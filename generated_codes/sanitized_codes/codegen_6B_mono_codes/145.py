
def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho, 
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    max_point = 0
    for index, num in enumerate(nums):
        temp_num = sum([int(x) for x in str(num)])
        ## toh max_point se max_point > temp_num or max_point < temp_num hona chaiye
        if max_point < temp_num:
            max_point = temp_num
            index_of_max_point = index

    ## agar sum(nums) and max_point > sum(nums) hona chaiye toh
    ## original index ke basis par, index_of_max_point bhi karte hai, and return karta hai
    if index_of_max_point < len(nums) - 1:
        return nums[index_of_max_point + 1:] + nums[:index_of_max_point + 1]
    return nums

    # return nums.sort(reverse=True)
    # return nums[index_of_max_point+1:] + nums[:index_of_max_point+1]

