# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 16:11:33
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            else:
                max_profit = max(prices[i] - lowest_price, max_profit)
        
        return max_profit