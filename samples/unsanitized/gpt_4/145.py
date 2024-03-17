Here is the Python function that fulfills the requirements:

```python
def order_by_points(nums):
    return sorted(nums, key=lambda x: (sum(int(d) for d in str(abs(x))), nums.index(x)))
```
This function sorts the list of integers based on the sum of their digits. If the sum of digits is the same for multiple numbers, it maintains their original order in the list. The `abs` function is used to handle negative numbers, as we need to consider the sum of the digits, not the sign.