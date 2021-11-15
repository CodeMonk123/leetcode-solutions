# -*- coding: utf-8 -*-
# @Date    : 2021-11-07 15:40:07
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        target = 0
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                target = i
                break
        
        return numbers[target]