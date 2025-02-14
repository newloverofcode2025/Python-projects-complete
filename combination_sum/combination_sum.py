def combinationSum3(k: int, n: int) -> list[list[int]]:
    """
    Find all valid combinations of k numbers that sum up to n using numbers from 1 to 9.
    Each number can only be used once.
    """
    def backtrack(start, path, remaining):
        # If the path length is k and the remaining sum is 0, we found a valid combination
        if len(path) == k and remaining == 0:
            result.append(path[:])
            return
        # If the path length is k or the remaining sum is negative, stop exploring this path
        if len(path) == k or remaining < 0:
            return
        # Explore further numbers
        for i in range(start, 10):
            path.append(i)
            backtrack(i + 1, path, remaining - i)
            path.pop()

    result = []
    backtrack(1, [], n)
    return result

if __name__ == "__main__":
    test_cases = [
        (3, 7),
        (3, 9),
        (4, 1)
    ]
    for k, n in test_cases:
        print(f"Combinations of {k} numbers that sum up to {n}: {combinationSum3(k, n)}")