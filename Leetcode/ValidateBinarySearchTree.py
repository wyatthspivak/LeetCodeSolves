import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, Tuple


class Solution:

    is_valid = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        bounds = (-math.inf, math.inf)
        self.dfs(root, bounds)
        return self.is_valid

    def dfs(self, node: Optional[TreeNode], bounds: Tuple[float, float]):
        if not node:
            return

        lower_bound = bounds[0]
        upper_bound = bounds[1]

        if lower_bound >= node.val or node.val >= upper_bound:
            self.is_valid = False

        self.dfs(node.left, (lower_bound, node.val))
        self.dfs(node.right, (node.val, upper_bound))


sol = Solution()

root_node = TreeNode(2)
root_node.left = TreeNode(2)
root_node.right = TreeNode(2)

print(sol.isValidBST(root_node))