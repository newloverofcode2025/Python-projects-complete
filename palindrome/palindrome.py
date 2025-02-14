def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.
    A palindrome is a string that reads the same forward and backward.
    """
    s = s.lower()  # Convert to lowercase to make the check case-insensitive
    s = ''.join(filter(str.isalnum, s))  # Remove non-alphanumeric characters
    return s == s[::-1]  # Compare the string with its reverse

if __name__ == "__main__":
    test_strings = ["A man, a plan, a canal, Panama", "racecar", "hello"]
    for test in test_strings:
        print(f"'{test}' is a palindrome: {is_palindrome(test)}")