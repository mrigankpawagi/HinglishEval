
def maximum(arr, k):
    """
    Ek array arr diya gaya hai integers ka aur ek positive integer k, return karo ek sorted list 
    lambai k ki maximum k numbers ke saath arr mein.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. Array ki lambai range mein hogi [1, 1000].
        2. Array ke elements range mein honge [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    arr = sorted(arr)
    return sorted(np.delete(np.delete(arr, k), -1), reverse=1)[:k]

print(maximum([-1, -4, 4], 2))

```

### Solution 1.8

```python
import statistics

