# -*- coding: utf-8 -*-
# @Date    : 2021-12-08 10:08:26
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < current_min:
                current_min = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - current_min)
        
        return max_profit