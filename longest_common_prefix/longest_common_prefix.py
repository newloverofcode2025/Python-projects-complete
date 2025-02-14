def longest_common_prefix(strs: list[str]) -> str:
    """
    Finds the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string.
    """
    if not strs:
        return ""

    # Sort the list of strings
    strs.sort()

    # Compare the first and last string in the sorted list
    first = strs[0]
    last = strs[-1]

    # Find the common prefix between the first and last string
    common_prefix = []
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            common_prefix.append(first[i])
        else:
            break

    return ''.join(common_prefix)

if __name__ == "__main__":
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["classroom", "class", "clasp"]
    ]
    for test in test_cases:
        print(f"Longest common prefix of {test}: '{longest_common_prefix(test)}'")