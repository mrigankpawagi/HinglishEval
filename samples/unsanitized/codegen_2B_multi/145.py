def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho,
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return [-1, -1, -1, -1, -1, -1]

    largest_number_so_far = max(nums)
    smallest_number_so_far = min(nums)

    sums = [0] * len(nums)
    for i in range(len(nums)):
        sums[i] = sums[i] + nums[i]

    sorted_nums = []
    if largest_number_so_far != 0:
        largest_smallest_index = 0
        while sorted_nums[largest_smallest_index] < largest_number_so_far:
            largest_smallest_index += 1

        sorted_nums = (
            sorted_nums[largest_smallest_index:] + sorted_nums[:largest_smallest_index]
        )

    for i in range(len(sorted_nums)):
        sums[i] = nums[i] - sum(sorted_nums[i:])
        if sums[i] != 0:
            sorted_nums.insert(i, sorted_nums[i] // sums[i])
            sorted_nums.insert(i, sorted_nums[i] % sums[i])

    return sorted_nums
