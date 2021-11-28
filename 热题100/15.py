# -*- coding: utf-8 -*-
# @Date    : 2021-11-28 14:55:50
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                temp = nums[j] + nums[k]
                if temp > target:
                    k -= 1
                elif temp < target:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        
        return [[x[0], x[1], x[2]] for x in res]