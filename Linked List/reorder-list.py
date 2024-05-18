class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        if head is None:
            return None

        def reverse(head):
            prev = None
            current_node = head

            while current_node:
                prev, prev.next, current_node = current_node, prev, current_node.next

            return prev

        def find_middle(head):
            fast = slow = head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            return slow

        middle = find_middle(head)
        reversed_half = reverse(middle.next)
        middle.next = None

        while reversed_half:
            head_next = head.next
            reversed_half_next = reversed_half.next
            head.next = reversed_half
            reversed_half.next = head_next
            reversed_half = reversed_half_next
            head = head_next


list_node = ListNode(10)
list_node.next = ListNode(30)
list_node.next.next = ListNode(40)
list_node.next.next.next = ListNode(3)

solution = Solution()
solution.reorderList(list_node)

while list_node:
    print(list_node.val, end=" -> ")
    list_node = list_node.next
print("None")
