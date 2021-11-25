# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 15:08:01
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            temp = nums[left] + nums[right]
            if  temp == target:
                return [nums[left], nums[right]]
            elif temp > target:
                right -= 1
            else:
                left += 1
        
        return []
