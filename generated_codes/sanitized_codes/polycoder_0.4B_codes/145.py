def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho,
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # return -sum(nums)
    order_list = []
    for item in nums:
        count = int([count2(item, nums[i]) for i, n in enumerate(nums[:-1])])
        if count == len(nums):
            # goo i i
            order_list.append(-sum([i.item() for i in nums]))
        elif count % 100:
            # goi igiigi igibh
            order_list.append(sum([i[i : i + 1] for i in nums]))
        else:
            # goi n i
            order_list.append(sum([i.item() for i in nums]))
    return order_list
