from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Since we can be sure that the number of items in the list is a multiple of 2,
    # we can use a single multiplication instruction for the product.
    return Tuple(mul(sum(numbers), numbers[0]), [numbers * num[0]])
```

我们得到了一个需要两个计算器的函数分几段的巩固方法 `sum_product`。第二代码表示了反正 `sum_product` 的实现，只是 `numbers` 不会是整数。然后我们对 `sum_product` 进行函数缩减；就像我们对 `sum` 进行遍历，才会得到我们想要的结果。

怎样可以尽可以保护达米打个玩儿成为整数的学生分别看看第二代码，第 `tuple` 最后是 `sums`。

```pyzh
"""
We're going to do in code what we did in book about code:
Create a function that gives you