# -*- coding: utf-8 -*-
# @Date    : 2021-10-15 14:10:39
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0 for _ in cost] + [0]
        min_cost[0] = 0
        min_cost[1] = 0

        for i in range(2, len(min_cost)):
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2])
        
        return min_cost[-1]