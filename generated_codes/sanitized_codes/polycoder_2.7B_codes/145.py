def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho,
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    res = []
    for n in nums:
        if n == 0:
            res.append(-1)
        else:
            ans = n * sum(n - i for i in range(1, len(nums) - 1))
            ans = ans % 11
            if not ans:
                ans = -1
                res.append(n)
            else:
                res[ans + 1] = n
    return res
