import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    """
    Merge k sorted linked lists into one sorted linked list.
    """
    # Define a comparison function for the heap
    ListNode.__lt__ = lambda self, other: self.val < other.val

    # Initialize a min-heap
    heap = []
    dummy = ListNode()
    current = dummy

    # Push the head of each list into the heap
    for linked_list in lists:
        if linked_list:
            heapq.heappush(heap, linked_list)

    # Merge the lists
    while heap:
        smallest_node = heapq.heappop(heap)
        current.next = smallest_node
        current = current.next
        if smallest_node.next:
            heapq.heappush(heap, smallest_node.next)

    return dummy.next

# Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next

if __name__ == "__main__":
    # Create linked lists
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    merged_list = mergeKLists([list1, list2, list3])
    print_linked_list(merged_list)