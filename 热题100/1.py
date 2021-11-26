# -*- coding: utf-8 -*-
# @Date    : 2021-11-26 16:28:30
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_with_index = sorted(zip(nums, list(range(len(nums)))))
        left,right = 0, len(nums) - 1
        while left < right:
            temp = num_with_index[left][0] + num_with_index[right][0]
            if temp == target:
                return [num_with_index[left][1], num_with_index[right][1]]
            elif temp > target:
                right -= 1
            else:
                left += 1
