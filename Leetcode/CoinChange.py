import math
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_change_memos = [-1] * ((10 ** 4) + 1)
        coin_change_memos[0] = 0

        for curr_amount in range(1, amount + 1):
            minimum_change = math.inf
            for coin in coins:
                if curr_amount - coin < 0:
                    continue
                if coin_change_memos[curr_amount - coin] != -1 and 1 + coin_change_memos[curr_amount - coin] < minimum_change:
                    minimum_change = 1 + coin_change_memos[curr_amount - coin]
            if minimum_change != math.inf:
                coin_change_memos[curr_amount] = minimum_change

        return coin_change_memos[amount]




sol = Solution()
print(sol.coinChange([2], 3))
