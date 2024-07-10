
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


    m, n = grid.shape
    if capacity == 0:
        return math.inf

    dp = [[-1 for _ in range(n)] for _ in range(m)]
    # dp[i][j] = i = row j = column mein pahile aane waali well hogi

    # base case
    for i in range(m):
        dp[i][0] = 0

    for i in range(m):
        for j in range(n):
            i1, j1 = i-1, j

            if grid[i][j] == 0:
                if i1 != -1:
                    dp[i][j] = dp[i1][j1] + 1
                if j1 != -1:
                    dp[i][j] = min(dp[i][j], dp[i1][j1])

            else: # wells
                if i1 == -1:
                    if j1 == -1:  # ye 2nd row wale corner well hai
                        dp[i][j] = -1
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][j1])
                        dp[i][j] = min(dp[i][j], dp[i1][j1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i1][j1])

    x = -1
    temp = math.inf
    for i in range(m):
        if dp[i][n-1] != -1:
            temp = min(temp, dp[i][n-1])
        if temp < capacity:
            x = i
            break
    
    return x if x != -1 else 0

# Aapko ek rectangular grid di gayi hai jisme wells hain. Har row ek well ko represent karhti hai,
# aur row me har 1 ek unit water ko represent karta hai. Har well ke paas ek corresponding bucket hoti hai
# jiska use usme se water extract karne ke liye kiya ja sakta hai, aur saare buckets ka capacity same hota hai.
# Aapka task hai buckets ka use karke