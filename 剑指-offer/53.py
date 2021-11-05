# -*- coding: utf-8 -*-
# @Date    : 2021-11-04 15:22:10
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

    
    def missingNumber2(self, nums:List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == mid:
                start = mid + 1
            else:
                end = mid - 1
        return start

solution = Solution()
print(solution.missingNumber2([0,1,3]))
print(solution.missingNumber2([1]))
print(solution.missingNumber2([0,1,2,3,4,5,6,7,9]))
print(solution.missingNumber2([0]))