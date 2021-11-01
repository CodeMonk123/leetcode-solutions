# -*- coding: utf-8 -*-
# @Date    : 2021-10-29 14:30:45
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length = 1
        current_length = 1
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i-1]:
                current_length += 1
            else:
                max_length = max(current_length, max_length)
                current_length = 1
        
        max_length = max(current_length, max_length)
        return max_length
            