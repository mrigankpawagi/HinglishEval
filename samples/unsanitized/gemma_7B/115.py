def max_fill(grid, capacity):
    import math

    """
    Aapko ek rectangular grid di gayi hai jisme wells hain. Har row ek well ko represent karti hai,
    aur row me har 1 ek unit water ko represent karta hai.
    Har well ke paas ek corresponding bucket hoti hai jiska use usme se water extract karne ke liye kiya ja sakta hai, 
    aur saare buckets ka capacity same hota hai.
    Aapka task hai buckets ka use karke wells ko empty karna.
    Output me aapko ye batana hai ki kitni baar aapko buckets ko lower karna padega.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * saare wells ka length same hota hai
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    # Write your code here
    # return the minimum number of times the bucket needs to be lowered

    # Approach:
    # 1. Find the max height of the grid
    # 2. Find the max height of the grid with the bucket capacity
    # 3. Find the difference between the two
    # 4. Return the difference

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)

    max_height = 0
    for row in grid:
        max_height = max(max_height, max(row))

    max_height_with_bucket = 0
    for row in grid:
        max_height_with_bucket = max(
            max_height_with_bucket, max_height_with_bucket + capacity - row[0]
        )

    return max_height - max_height_with_bucket
