from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum_solution_list = []
        solution_set = set()

        # for every number in nums, take its negative and treat it as a target in 2sum

        for i in range(len(nums)):
            target = -nums[i]
            solution_map = {}

            for j in range(len(nums)):
                solution = target - nums[j]
                if solution in solution_map and solution_map[solution] != i and solution_map[solution] != j and i != j:
                    solution_list = [nums[i], nums[j], solution]
                    solution_list.sort()
                    solution_tuple = tuple(solution_list)

                    if solution_tuple not in solution_set:
                        three_sum_solution_list.append(solution_list)
                        solution_set.add(solution_tuple)
                solution_map[nums[j]] = j

        return three_sum_solution_list


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
