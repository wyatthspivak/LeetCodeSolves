from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []

        intervals.sort(key=lambda x: x[0])

        curr_start = intervals[0][0]
        curr_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start > curr_end:
                merged_intervals.append([curr_start, curr_end])
                curr_start = start
                curr_end = end

            elif start >= curr_start and end <= curr_end:
                continue

            elif start <= curr_end:
                curr_end = end

        merged_intervals.append([curr_start, curr_end])

        return merged_intervals



