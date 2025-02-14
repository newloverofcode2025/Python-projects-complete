def solve(board: list[list[str]]) -> None:
    """
    Capture all regions surrounded by 'X'.
    """
    if not board:
        return

    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'T'  # Mark as temporarily safe
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # Mark 'O's on the border and their connected components as temporarily safe
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    # Flip all 'O's to 'X's, and restore the temporarily safe 'O's
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'T':
                board[r][c] = 'O'

if __name__ == "__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    solve(board)
    for row in board:
        print(row)