class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeNthFromEnd(head, n):
    result = ListNode(0, head)
    dummy = result

    for _ in range(n):
        head = head.next

    while head:
        head = head.next
        dummy = dummy.next

    dummy.next = dummy.next.next

    return result.next
