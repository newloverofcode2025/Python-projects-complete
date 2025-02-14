class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

def findWords(board, words):
    def backtrack(node, row, col, prefix):
        if node.is_end_of_word:
            result.add(prefix)
        char = board[row][col]
        board[row][col] = '#'  # Mark as visited
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] in node.children:
                backtrack(node.children[board[r][c]], r, c, prefix + board[r][c])
        board[row][col] = char  # Restore the cell

    trie = Trie()
    for word in words:
        trie.insert(word)
    
    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in trie.root.children:
                backtrack(trie.root.children[board[i][j]], i, j, board[i][j])
    
    return list(result)

if __name__ == "__main__":
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(f"Words found in the board: {findWords(board, words)}")