class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def reverse_list(head):
    if not head or not head.next:
        return head

    prev_node = None
    while head:
        temp_node = head.next
        head.next = prev_node
        head.prev = temp_node
        prev_node = head
        head = temp_node

    return prev_node


node1 = ListNode(10)
node2 = ListNode(15)
node3 = ListNode(20)
node4 = ListNode(25)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

new_head = reverse_list(node1)

while new_head:
    print(new_head.val, end=" <-> ")
    new_head = new_head.next
print(None)
