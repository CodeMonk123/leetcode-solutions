# -*- coding: utf-8 -*-
# @Date    : 2021-12-03 14:44:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
        
        for i in range(count_0):
            nums[i] = 0
        
        for i in range(count_0, count_0 + count_1):
            nums[i] = 1
        
        for i in range(count_0+count_1, len(nums)):
            nums[i] = 2
            