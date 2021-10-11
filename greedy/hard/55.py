# -*- coding: utf-8 -*-
# @Date    : 2021-10-11 10:48:36
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        target = len(nums) - 1
        current = target - 1
        while current >= 0:
            if current + nums[current] >= target:
                target = current
            current -= 1
        
        return target == 0


solution = Solution()
print(solution.canJump([2,3,1,1,4]))
print(solution.canJump([3,2,1,0,4]))
