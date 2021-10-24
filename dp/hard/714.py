# -*- coding: utf-8 -*-
# @Date    : 2021-10-24 16:06:56
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profits = [[0,0] for _ in prices]
        profits[0][0] = -prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profits[i][0] = max(profits[i-1][0], profits[i-1][1] - prices[i])
            profits[i][1] = max(profits[i-1][0] + prices[i] - fee, profits[i-1][1])
            max_profit = max(max_profit, profits[i][1])
        
        return max_profit

solution = Solution()
print(solution.maxProfit([1,3,7,5,10,3], 3))