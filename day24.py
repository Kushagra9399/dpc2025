'''
You are given a binary tree and two distinct nodes within the tree. Your task is to find the lowest common ancestor (LCA) of these two nodes. The LCA of two nodes p and q is defined as the lowest node in the tree that has both p and q as descendants (where we allow a node to be a descendant of itself).
Input:
A binary tree represented as a series of nodes where each node has references to its left and right child.
Two distinct nodes p and q from the tree.
Output:
Return the node that is the lowest common ancestor (LCA) of p and q.
Examples:
Example 1
Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
Output: 3
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

def day24_sol(root, p, q):
    if not root or root == p or root == q:
        return root
    left = day24_sol(root.left, p, q)
    right = day24_sol(root.right, p, q)
    if left and right:
        return root
    return left if left else right

root = build_tree( [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = find_node(root, 5)
q = find_node(root, 1)
print(day24_sol(root, p, q).val)
