# -*- coding: utf-8 -*-
# @Date    : 2021-11-30 10:48:03
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            if nums[0] <= nums[mid]:
                if nums[0] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            
            else:
                if nums[mid] < target and target <= nums[-1]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1

solution = Solution()
print(solution.search(nums = [4,5,6,7,0,1,2], target = 0))
print(solution.search(nums = [3,1], target = 1))