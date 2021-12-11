# -*- coding: utf-8 -*-
# @Date    : 2021-12-09 11:15:03
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = [num for num in nums]
        min_prod = [num for num in nums]

        

        for i in range(1, len(nums)):
            max_prod[i] = max(max_prod[i-1] * nums[i], max(nums[i], min_prod[i-1] * nums[i]))
            min_prod[i] = min(max_prod[i-1] * nums[i], min(nums[i], min_prod[i-1] * nums[i]))
        
        return max(max_prod)

solution = Solution()
print(solution.maxProduct([2,3,-2,4]))
print(solution.maxProduct([-2]))