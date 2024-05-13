import heapq


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_k_lists(lists):
    values = []

    for node in lists:
        while node:
            values.append(node.value)
            node = node.next
    
    if not values:
        return None
    
    heapq.heapify(values)
    dummy = ListNode(0)
    current = dummy

    while values:
        value = heapq.heappop(values)
        current.next = ListNode(value)
        current = current.next

    return dummy.next
