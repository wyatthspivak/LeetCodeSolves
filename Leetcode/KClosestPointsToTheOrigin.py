import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        k_smallest_points = []

        for point in points:
            dis = self.computeDistanceSquared(point)
            point_dis_pair = (dis, point)
            heapq.heappush(min_heap, point_dis_pair)

        for i in range(k):
            smallest_distance, smallest_point = heapq.heappop(min_heap)
            k_smallest_points.append(smallest_point)

        return k_smallest_points


    def computeDistanceSquared(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]

        return x * x + y * y


sol = Solution()

sol.kClosest([[1,3],[-2,2]], 1)