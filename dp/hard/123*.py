# -*- coding: utf-8 -*-
# @Date    : 2021-10-24 14:22:27
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits: List[List[int]] = [[0,0,0,0] for _ in prices]
        # profits[i][j]
        # j = 0: 第一次买入 1: 第一次卖出, 2: 第二次买入, 3: 第二次卖出
        profits[0][0] = -prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profits[i][0] = max(profits[i-1][0], -prices[i])
            profits[i][1] = max(profits[i-1][1], profits[i-1][0] + prices[i])
            if i >= 2:
                profits[i][2] = profits[i-1][1] - prices[i]
                if i > 2:
                    profits[i][2] = max(profits[i][2], profits[i-1][2])
                    profits[i][3] = profits[i-1][2] + prices[i]
                    if i > 3:
                        profits[i][3] = max(profits[i-1][3], profits[i][3])
            max_profit = max(max_profit, profits[i][3], profits[i][1])

        
        return max_profit

solution = Solution()
# print(solution.maxProfit([3,3,5,0,0,3,1,4]))
print(solution.maxProfit([1,2,3,4,5]))