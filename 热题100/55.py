# -*- coding: utf-8 -*-
# @Date    : 2021-12-01 10:49:19
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        can_jump = [False for _ in nums]
        can_jump[-1] = True
        start = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= start:
                start = i
                can_jump[i] = True

        return can_jump[0]

solution = Solution()
print(solution.canJump([2,3,1,1,4]))
print(solution.canJump([3,2,1,0,4]))