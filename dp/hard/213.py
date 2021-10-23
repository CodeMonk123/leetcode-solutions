# -*- coding: utf-8 -*-
# @Date    : 2021-10-23 15:58:32
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def _rob(self, nums:List[int]) -> int:
        max_value1 = [0 for _ in nums]
        max_value2 = [0 for _ in nums]
        max_value1[0] = nums[0]
        for i in range(1, len(nums)):
            max_value1[i] = nums[i] + max(max_value2[i-1], max_value1[i-2] if i >= 2 else 0)
            max_value2[i] = max(max_value2[i-1], max_value1[i-1])
        
        return max(max_value1[-1], max_value2[-1])

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))

solution = Solution()
print(solution.rob([2,3,2]))
