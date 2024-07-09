def minPath(grid, k):
    N = len(grid)
    min_val = min(min(row) for row in grid)
    min_val_indices = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == min_val]
    min_path = [min_val]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for _ in range(k - 1):
        next_min_val = float('inf')
        next_min_val_indices = []

        for x, y in min_val_indices:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] < next_min_val:
                    next_min_val = grid[nx][ny]
                    next_min_val_indices = [(nx, ny)]
                elif 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == next_min_val:
                    next_min_val_indices.append((nx, ny))

        min_val = next_min_val
        min_val_indices = next_min_val_indices
        min_path.append(min_val)

    return min_path