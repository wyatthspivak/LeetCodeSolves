from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = []
    max_distance = 0
    node_distances = {}

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result.clear()
        self.node_distances.clear()

        if not root:
            return self.result

        self.traverse(root, 0)

        for i in range(self.max_distance + 1):
            self.result.append([])
            for val in self.node_distances[i]:
                self.result[i].append(val)

        return self.result

    def traverse(self, node: Optional[TreeNode], distance_from_root: int) -> None:
        if not node:
            return

        self.max_distance = max(distance_from_root, self.max_distance)

        if distance_from_root not in self.node_distances:
            self.node_distances[distance_from_root] = [node.val]
        else:
            self.node_distances[distance_from_root].append(node.val)

        self.traverse(node.left, distance_from_root + 1)
        self.traverse(node.right, distance_from_root + 1)



sol = Solution()
root = TreeNode(1)

print(sol.levelOrder(root))
