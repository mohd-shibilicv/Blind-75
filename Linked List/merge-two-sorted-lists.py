class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    current_node = dummy

    while list1 and list2:
        if list1.value < list2.value:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next
        current_node = current_node.next

    if list1:
        current_node.next = list1
    if list2:
        current_node.next = list2

    return dummy.next


list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(6)

merged_list = merge_two_lists(list1, list2)
while merged_list:
    print(merged_list.value)
    merged_list = merged_list.next
