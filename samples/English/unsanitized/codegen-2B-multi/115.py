
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

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
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    M = len(grid)
    N = len(grid[0])
    result = 0 if N < 2 else 0
    for m in range(M-1, -1, -1):
        for n in range(N-1, -1, -1):
            try:
                if grid[m][n] == 1:
                    for i in range(M-m):                                                           # check if i step down
                        if grid[i][n]!= 1: continue                                                # if not, check i+1
                        for j in range(N-n):                                                        # check if j step down
                            if grid[m+1][j]!= 1: continue                                          # if not, check