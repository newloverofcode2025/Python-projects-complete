## Word Search

### Description
Given an m x n grid of characters board and a string word, return True if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example
Input:
board = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]
word = "ABCCED"
Output: True
Input:
board = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]
word = "SEE"
Output: True
Input:
board = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]
word = "ABCB"
Output: False
A function to determine if the word exists in the board.

### File
- [word_search.py](word_search.py)
Run the code in VS Code by pressing F5 or by clicking the "Run" button in the top-right corner.
Verify the output:
Word 'ABCCED' exists in the board: True
Word 'SEE' exists in the board: True
Word 'ABCB' exists in the board: False
