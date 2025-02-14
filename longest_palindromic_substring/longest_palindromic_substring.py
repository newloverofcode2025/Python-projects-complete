def longestPalindrome(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    """
    def expandAroundCenter(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 1:
        return ""

    start, end = 0, 0
    for i in range(len(s)):
        len1 = len(expandAroundCenter(i, i))  # Odd length palindrome
        len2 = len(expandAroundCenter(i, i + 1))  # Even length palindrome
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

if __name__ == "__main__":
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "ac"
    ]
    for test in test_cases:
        print(f"Longest palindromic substring in '{test}': '{longestPalindrome(test)}'")