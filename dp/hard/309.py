# -*- coding: utf-8 -*-
# @Date    : 2021-10-24 15:24:03
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profits = [[0,0] for _ in prices]
        profits[0][0] = -prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profits[i][0] = max(profits[i-1][0], (profits[i-2][1] if i > 2 else 0) - prices[i])
            profits[i][1] = max(profits[i-1][1], profits[i-1][0] + prices[i])
            max_profit = max(max_profit, profits[i][1])
        # print(profits)
        return max_profit

solution = Solution()
# print(solution.maxProfit([1,2,3,0,2]))
# print(solution.maxProfit([2,1,4]))
print(solution.maxProfit([6,1,3,2,4,7]))
    