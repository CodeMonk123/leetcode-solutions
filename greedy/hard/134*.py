# -*- coding: utf-8 -*-
# @Date    : 2021-10-15 10:48:02
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_add = [x[0] - x[1] for x in zip(gas, cost)]
        if sum(gas_add) < 0 :
            return -1
        
        start = 0
        current_sum = 0
        total_sum = 0
        for i, v in enumerate(gas_add):
            current_sum += v
            if current_sum < 0:
                current_sum = 0
                start = i + 1
            total_sum += v
        
        if total_sum < 0:
            return -1
        return start