from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create right product array
        right_product = [1] * len(nums)
        left_product = [1] * len(nums)
        cur = 1
        for i in range(len(nums) - 1, 0, -1):
            cur *= nums[i]
            right_product[i - 1] = cur

        cur = 1
        for i in range(0, len(nums) - 1):
            cur *= nums[i]
            left_product[i + 1] = cur

        answers = []
        for i in range(len(nums)):
            answers.append(right_product[i] * left_product[i])

        return answers


sol = Solution()

print(sol.productExceptSelf([-1,1,0,-3,3]))

