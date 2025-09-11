'''
You are given the root of a binary tree. Your task is to determine whether the tree is symmetric. A binary tree is symmetric if the left and right subtrees are mirror images of each other.
Input:
The root of the binary tree.
Output:
Return true if the binary tree is symmetric, otherwise return false.
Examples:
Example 1
Input: [1, 2, 2, 3, 4, 4, 3]
Output: true
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    arr = [root]
    i = 1
    while i < len(values) and arr:
        curr = arr.pop(0)
        if values[i] is not None:
            node = TreeNode(values[i])
            curr.left = node
            arr.append(node)
        i += 1
        if i < len(values) and values[i] is not None:
            node = TreeNode(values[i])
            curr.right = node
            arr.append(node)
        i += 1
    return root

def day28_sol(root):
    if root is None:
        return True
    left_tree = [root.left]
    right_tree = [root.right]
    while left_tree or right_tree:
        if not left_tree or not right_tree:
            return False
        left = left_tree.pop(0)
        right = right_tree.pop(0)
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        left_tree.append(left.left)
        left_tree.append(left.right)
        right_tree.append(right.right)
        right_tree.append(right.left)
    return True
    
root = create_tree([1, 2, 2, 3, 4, 4, 3])
print(day28_sol(root))
