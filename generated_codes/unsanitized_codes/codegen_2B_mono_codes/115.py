
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
    m, n = len(grid), len(grid[0])
    B = [[] for _ in range(m)]

    # fill bucket as per the directions given
    for i in range(m):
        for j in range(n):
            B[i].append(math.inf)

    # first row
    B[0][0] = min(B[i][j] for i in range(0, m) for j in range(0, n) if