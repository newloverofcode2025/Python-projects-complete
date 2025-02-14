def minCut(s: str) -> int:
    """
    Find the minimum number of cuts needed for a palindrome partitioning of s.
    """
    n = len(s)
    # dp[i] will be the minimum cuts needed for a palindrome partitioning of s[:i+1]
    dp = [float('inf')] * n
    # p[i][j] will be True if the substring s[i:j+1] is a palindrome
    p = [[False] * n for _ in range(n)]

    for i in range(n):
        # Every single character is a palindrome
        p[i][i] = True
        if i > 0 and s[i] == s[i - 1]:
            p[i - 1][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and p[i + 1][j - 1]:
                p[i][j] = True

    for i in range(n):
        if p[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if p[j + 1][i] and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1

    return dp[n - 1]

if __name__ == "__main__":
    test_cases = [
        "aab",
        "a",
        "ab"
    ]
    for test in test_cases:
        print(f"Minimum cuts needed for palindrome partitioning of '{test}': {minCut(test)}")