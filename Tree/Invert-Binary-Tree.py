class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root):
    if not root:
        return None

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    root.left, root.right = root.right, root.left

    return root


def inorder_traversal(root, result):

    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)

    return result


root = ListNode(5)
root.left = ListNode(4)
root.right = ListNode(6)
root.left.left = ListNode(3)
root.left.right = ListNode(5)
root.right.left = ListNode(2)
root.right.right = ListNode(8)

actual_tree = inorder_traversal(root, [])
print(actual_tree)

inverted_root = invert_binary_tree(root)

inverted_tree = inorder_traversal(inverted_root, [])
print(inverted_tree)
