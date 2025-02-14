def maxSumSubmatrix(matrix: list[list[int]]) -> int:
    """
    Find the maximum sum of any submatrix in a given matrix.
    """
    def kadane(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]
            max_sum = max(max_sum, kadane(temp))

    return max_sum

if __name__ == "__main__":
    matrix = [
        [1, -2, -3, 4],
        [-5, -6, -7, -8],
        [9, 10, 11, 12]
    ]
    print(f"Maximum sum of any submatrix in the given matrix: {maxSumSubmatrix(matrix)}")