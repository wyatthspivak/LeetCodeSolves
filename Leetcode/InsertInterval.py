from typing import List


class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals_with_new = []

        new_interval_start = newInterval[0]

        inserted = False

        if len(intervals) == 0:
            intervals_with_new.append(newInterval)
            return intervals_with_new

        for i in range(len(intervals) + 1):
            if inserted:
                curr_start = intervals[i - 1][0]
            elif i == len(intervals):
                curr_start = new_interval_start + 1
            else:
                curr_start = intervals[i][0]

            if curr_start > new_interval_start and not inserted:
                intervals_with_new.append(newInterval)
                inserted = True

            elif inserted:
                intervals_with_new.append(intervals[i - 1])

            else:
                intervals_with_new.append(intervals[i])

        return self.merge(intervals_with_new)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []

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


sol = Solution()

print(sol.insert([[1, 5]], [2, 3]))
