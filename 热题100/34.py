# -*- coding: utf-8 -*-
# @Date    : 2021-11-30 11:07:16
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def _binary_search_left(self, nums:List[int], target:int)->int:
        start, end = 0, len(nums) - 1
        left_most_index = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    left_most_index = mid
                    break
                else:
                    end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1                     
        return left_most_index

    def _binary_search_right(self, nums:List[int], target:int)->int:
        start, end = 0, len(nums) - 1
        right_most_index = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid+1] != target:
                    right_most_index = mid
                    break
                else:
                    start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1                     
        return right_most_index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self._binary_search_left(nums, target), self._binary_search_right(nums, target)]


solution = Solution()
print(solution.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(solution.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(solution.searchRange(nums = [2,2], target = 2))