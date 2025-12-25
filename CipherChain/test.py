class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order_traversal(root):
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.data, end=" ")
    in_order_traversal(root.right)

def pre_order_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)

def post_order_traversal(root):
    if root is None:
        return
        post_order_traversal(root.left)
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.data, end=" ")

from collections import deque

def level_order_traversal(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node.data, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("In-Order Traversal:")
in_order_traversal(root)

print("\n\nPre-Order Traversal:")
pre_order_traversal(root)

print("\n\nPost-Order Traversal:")
post_order_traversal(root)

print("\n\nLevel-Order Traversal:")
level_order_traversal(root)

print("\n\nTotal Nodes:")
print(count_nodes(root))

print("\nHeight of Tree:")
print(height(root))
