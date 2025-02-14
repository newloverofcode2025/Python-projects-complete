from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    """
    Find the length of the shortest transformation sequence from beginWord to endWord.
    """
    if endWord not in wordList:
        return 0

    word_set = set(wordList)
    queue = deque([beginWord])
    level = 0

    while queue:
        level += 1
        size = len(queue)
        current_level = set()

        for _ in range(size):
            current_word = queue.popleft()
            if current_word == endWord:
                return level

            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i + 1:]
                    if next_word in word_set:
                        queue.append(next_word)
                        current_level.add(next_word)
                        word_set.remove(next_word)

        word_set -= current_level

    return 0

if __name__ == "__main__":
    test_cases = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        ("hot", "dog", ["hot", "dog"]),
        ("a", "c", ["a", "b", "c"])
    ]
    for beginWord, endWord, wordList in test_cases:
        print(f"Shortest transformation length from '{beginWord}' to '{endWord}': {ladderLength(beginWord, endWord, wordList)}")