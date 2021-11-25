# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 15:10:17
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        end = len(nums)
        for i in range(start, len(nums)):
            if nums[i] != target:
                end = i
                break
        
        return end - start

print(Solution().search([5,7,7,8,8,8,10,10,10], 5))
print(Solution().search([5,7,7,8,8,8,10,10,10], 7))
print(Solution().search([5,7,7,8,8,8,10,10,10], 8))
print(Solution().search([5,7,7,8,8,8,10,10,10], 10))