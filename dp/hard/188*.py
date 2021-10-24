# -*- coding: utf-8 -*-
# @Date    : 2021-10-24 14:54:24
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k == 0:
            return 0 
        profits = [[0 for _ in range(2*k)] for _ in prices]
        max_profit = 0

        profits[0][0] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(min(i + 1, 2*k)):
                if j % 2 == 0: # 买入
                    profits[i][j] = -prices[i] + (profits[i-1][j-1] if j > 0 else 0)
                    if j < min(i+1, 2*k) - 1:
                        profits[i][j] = max(profits[i][j], profits[i-1][j])
                else: # 卖出
                    profits[i][j] = max(profits[i-1][j], prices[i] + profits[i-1][j-1])
                    max_profit = max(max_profit, profits[i][j])
        # print(profits)
        return max_profit

solution = Solution()
# print(solution.maxProfit(2, [2,4,1]))
# print(solution.maxProfit(2, [3,2,6,5,0,3]))
# print(solution.maxProfit(2, [1,2,4]))
print(solution.maxProfit(2, [3,3,5,0,0,3,1,4]))