# -*- coding: utf-8 -*-
# @Date    : 2021-10-24 14:05:13
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [[0,0] for _ in prices]
        profits[0][0] = -prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profits[i][0] = max(profits[i-1][1] - prices[i], profits[i-1][0])
            profits[i][1] = max(profits[i-1][0] + prices[i], profits[i-1][1])
            max_profit = max(max_profit, profits[i][1])
        # print(profits)
        return max_profit
    
solution = Solution()
# print(solution.maxProfit([7,1,5,3,6,4]))
# print(solution.maxProfit([7,6,5,4,3,2,1]))
# print(solution.maxProfit([1,2,3,4,5]))
print(solution.maxProfit([3,2,6,5,0,3]))