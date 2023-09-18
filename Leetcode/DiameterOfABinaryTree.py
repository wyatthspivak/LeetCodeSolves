from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse_tree(root)
        return self.diameter

    def traverse_tree(self, node: Optional[TreeNode]) -> int:
        left_height, right_height = 0, 0
        if node is None:
            return 0

        if node.right:
            right_height = self.traverse_tree(node.right)
        if node.left:
            left_height = self.traverse_tree(node.left)

        self.diameter = max(self.diameter, right_height + left_height)

        return 1 + max(left_height, right_height)
