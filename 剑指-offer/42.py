# -*- coding: utf-8 -*-
# @Date    : 2021-11-05 10:32:13
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        
        partial_sum = 0
        max_sum = 0

        for num in nums:
            partial_sum = max(0, partial_sum + num)
            max_sum = max(partial_sum, max_sum)
        
        return max_sum
