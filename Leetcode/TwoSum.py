class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # We pass through the list and store every number with a corresponding index
        # As we iterate through, we check if the corresponding Target - Current Number is in the
        # dictionary, if it is, we can return it

        solution_store = {}

        for i in range(len(nums)):
            curr_num = nums[i]
            solution = target - curr_num
            if solution in solution_store:
                return [solution_store[solution], i]
            solution_store[curr_num] = i


two_sum_test = Solution()
print(two_sum_test.twoSum([3, 3], 6))
