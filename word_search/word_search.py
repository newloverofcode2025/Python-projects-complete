def exist(board: list[list[str]], word: str) -> bool:
    """
    Determine if the word exists in the board.
    """
    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def backtrack(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        temp, board[r][c] = board[r][c], '#'
        for dr, dc in directions:
            if backtrack(r + dr, c + dc, index + 1):
                return True
        board[r][c] = temp
        return False

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False

if __name__ == "__main__":
    test_cases = [
        ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCCED"),
        ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "SEE"),
        ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCB")
    ]
    for board, word in test_cases:
        print(f"Word '{word}' exists in the board: {exist(board, word)}")