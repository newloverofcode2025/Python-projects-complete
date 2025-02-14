def length_of_LIS(nums: list[int]) -> int:
    """
    Find the length of the longest increasing subsequence in an array.
    """
    if not nums:
        return 0

    # Initialize the dp array where dp[i] represents the length of the longest increasing subsequence
    # that ends with nums[i]
    dp = [1] * len(nums)

    # Fill dp array
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest increasing subsequence is the maximum value in dp array
    return max(dp)

if __name__ == "__main__":
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7]
    ]
    for test in test_cases:
        print(f"The length of the longest increasing subsequence in {test} is: {length_of_LIS(test)}")