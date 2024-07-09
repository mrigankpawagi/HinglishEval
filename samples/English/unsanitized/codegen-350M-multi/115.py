
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
    def is_valid(grid):
        l = len(grid)
        if l < 1:
            return False
        if l!= (grid[0][0]).get() or \
            grid[0][1].get()!= grid[1][1].get():
            return False
        for i in range(l):
            if (grid[i][0].get() == 0 or grid[i][1].get() == 0) or \
                    (grid[i][0].get() == grid[i][1].get() == 1):
                return False
        return True

    capacity = int(abs(grid[1][1].get()) - grid[0][1].get())
    bucket_size = capacity / 2 + 1
    count = 1
    