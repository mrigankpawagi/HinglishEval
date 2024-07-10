
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
    n, m, s, bucket_capacity = len(grid), len(grid[0]), 0, capacity

    def get_empty_well(wells, index):
        for well in wells:
            if well == 0:
                return index
        return 0

    grid = [list(row) for row in grid]
    # Initialize empty bucket index at each row's index
    empty_buckets = [[0] * n for _ in range(n)]
    # Go through every grid row
    for i in range(0, n):
        # Go through each grid well's value
        for j in range(0, m):
            # If this well has enough water in it to be filled
            if grid[i][j]:
                # Count bucket indices that are empty
                empty_buckets[i][j] = get_empty_well(empty_buckets[i], j)
                grid[i][j] -= 1
                # Otherwise add this bucket's index to grid's water bucket
                if empty_buckets[i][j] > bucket_capacity:
                    grid[i][j] -= bucket_capacity
                    empty_buckets[i][j] = -1
    return s
if __name__ == "__main__":
    m, n, capacity = [int(x) for x in input().split()]
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(max_fill(grid, capacity))
