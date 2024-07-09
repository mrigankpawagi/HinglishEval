```python
def minPath(grid, k):
    N = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j] = [grid[i][j]]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < N and 0 <= y < N and dp[x][y]:
                    dp[i][j] = min(dp[i][j], [grid[i][j]] + dp[x][y][:k-1])
    return min(dp[i][j] for i in range(N) for j in range(N) if len(dp[i][j]) == k)
```