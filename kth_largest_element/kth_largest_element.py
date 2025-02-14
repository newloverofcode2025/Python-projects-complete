import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Find the kth largest element in an unsorted list.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    """
    # Use a min-heap to keep track of the k largest elements seen so far
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
    
    # The root of the min-heap is the kth largest element
    return min_heap[0]

if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    ]
    for nums, k in test_cases:
        print(f"The {k}th largest element in {nums} is: {find_kth_largest(nums, k)}")