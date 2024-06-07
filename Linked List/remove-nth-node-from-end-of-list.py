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


list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)
list1.next.next.next = ListNode(10)
list1.next.next.next.next = ListNode(4)

new_list = removeNthFromEnd(list1, 2)
while new_list:
    print(new_list.value, end=" -> ")
    new_list = new_list.next
print("None")
