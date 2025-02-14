def combinationSum2(candidates: list[int], target: int, k: int) -> list[list[int]]:
    """
    Find all possible combinations of k numbers that sum up to target using numbers from candidates.
    Each number can only be used once. The solution set must not contain duplicate combinations.
    
    Args:
        candidates (list[int]): List of candidate numbers
        target (int): Target sum to achieve
        k (int): Number of elements required in each combination
        
    Returns:
        list[list[int]]: List of all valid combinations
    """
    def backtrack(start: int, path: list, remaining: int) -> None:
        # Base cases
        if len(path) == k:
            if remaining == 0:
                result.append(path[:])
            return
        
        if len(path) > k or remaining < 0:
            return
            
        for i in range(start, len(candidates)):
            # Skip duplicates to avoid duplicate combinations
            if i > start and candidates[i] == candidates[i - 1]:
                continue
                
            current = candidates[i]
            path.append(current)
            backtrack(i + 1, path, remaining - current)
            path.pop()  # backtrack
    
    # Sort candidates to handle duplicates efficiently
    candidates.sort()
    result = []
    backtrack(0, [], target)
    return result

def main():
    # Test cases
    test_cases = [
        ([10, 1, 2, 7, 6, 1, 5], 8, 3),  # Should find combinations
        ([2, 5, 2, 1, 2], 5, 2),         # No valid combinations
        ([1, 2, 3, 4, 5], 5, 2),         # Should find [1,4] and [2,3]
        ([1, 1, 1, 1, 2, 2, 3], 4, 3)    # Should find combinations
    ]
    
    for candidates, target, k in test_cases:
        result = combinationSum2(candidates, target, k)
        print(f"\nTest case:")
        print(f"Candidates: {candidates}")
        print(f"Target: {target}")
        print(f"K: {k}")
        print(f"Found combinations: {result}")

if __name__ == "__main__":
    main()