'''
You are given the root of a binary tree. Your task is to determine whether the tree is a valid Binary Search Tree (BST). A binary search tree is defined as a tree where:
Every node’s left subtree contains only nodes with values less than the node’s value.
Every node’s right subtree contains only nodes with values greater than the node’s value.
Both the left and right subtrees must also be binary search trees.
Input:
A binary tree represented by its root node.
Output:
Return true if the binary tree is a valid BST, otherwise return false.
Examples:
Example 1
Input: root = [2, 1, 3]
Output: true
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
    
def day25_sol(root):
    def validate(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
    
    return validate(root, float('-inf'), float('inf'))

root = build_tree([2,1,3])
print(day25_sol(root))
