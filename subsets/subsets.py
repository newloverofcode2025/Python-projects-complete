def subsets(nums: list[int]) -> list[list[int]]:
    """
    Find all possible subsets of a given set.
    """
    def backtrack(start, path):
        # Add the current subset to the result
        result.append(path[:])
        # Explore further elements to add to the current subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [0],
        [4, 1, 0]
    ]
    for test in test_cases:
        print(f"Subsets of {test}: {subsets(test)}")