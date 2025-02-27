def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    """
    m, n = len(text1), len(text2)
    # Initialize the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

if __name__ == "__main__":
    test_cases = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def")
    ]
    for text1, text2 in test_cases:
        print(f"Longest common subsequence length between '{text1}' and '{text2}': {longestCommonSubsequence(text1, text2)}")