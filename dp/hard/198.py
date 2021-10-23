# -*- coding: utf-8 -*-
# @Date    : 2021-10-23 15:49:59
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def rob(self, nums: List[int]) -> int:
        max_value1 = [0 for _ in nums]
        max_value2 = copy.deepcopy(max_value1)

        max_value1[0] = nums[0]
        for i in range(1, len(nums)):
            max_value1[i] = max(max_value2[i-1], max_value1[i-2] if i > 1 else 0)  + nums[i]
            max_value2[i] = max(max_value1[i-1], max_value2[i-1])
        
        return max(max_value1[-1], max_value2[-1])

solution = Solution()

print(solution.rob([2,7,9,3,1]))