def minPathSum(grid: list[list[int]]) -> int:
    """
    Find the minimum path sum in a grid.
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    
    # Initialize the first row and first column
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]
    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]

    # Fill the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[m - 1][n - 1]

if __name__ == "__main__":
    test_cases = [
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
        [[1, 2, 3], [4, 5, 6]]
    ]
    for grid in test_cases:
        print(f"Minimum path sum in grid {grid}: {minPathSum(grid)}")