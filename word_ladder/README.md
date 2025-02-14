## Word Ladder

### Description
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note that beginWord is not a transformed word.
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

A function to find the length of the shortest transformation sequence from beginWord to endWord.

### File
- [word_ladder.py](word_ladder.py)
Run the code in VS Code by pressing F5 or by clicking the "Run" button in the top-right corner.
Verify the output:
Shortest transformation length from 'hit' to 'cog': 5
Shortest transformation length from 'hot' to 'dog': 3
Shortest transformation length from 'a' to 'c': 2
