# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
import queue


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_queue = queue.Queue()
        cloned_node_queue = queue.Queue()

        if not node:
            return node

        current_cloned_node = Node(node.val)

        node_queue.put(node)
        cloned_node_queue.put(current_cloned_node)

        visited = set()
        cloned_node_lookup = {current_cloned_node.val: current_cloned_node}

        visited.add(node.val)

        while node_queue.qsize() > 0:
            current_node = node_queue.get()
            current_cloned_node = cloned_node_queue.get()

            cloned_node_neighbor_list = []

            for neighbor in current_node.neighbors:
                if neighbor.val not in cloned_node_lookup:
                    cloned_neighbor = Node(neighbor.val)
                else:
                    cloned_neighbor = cloned_node_lookup[neighbor.val]
                cloned_node_neighbor_list.append(cloned_neighbor)

                # add cloned neighbors to cloned_node_queue and regular neighbors to node_queue
                if neighbor.val not in visited:
                    cloned_node_queue.put(cloned_neighbor)
                    node_queue.put(neighbor)
                    visited.add(neighbor.val)
                    cloned_node_lookup[neighbor.val] = cloned_neighbor

            current_cloned_node.neighbors = cloned_node_neighbor_list

        return cloned_node_lookup[node.val]


sol = Solution()

head_node = Node()