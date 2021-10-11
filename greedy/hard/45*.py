# -*- coding: utf-8 -*-
# @Date    : 2021-10-11 10:54:25
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def jump(self, nums: List[int]) -> int:

        max_distance = 0
        cur_distance = 0
        count = 0
        for i in range(len(nums)):
            max_distance = max(max_distance, nums[i] + i)
            if max_distance >= len(nums) - 1:
                count += 1
                break
            if i == cur_distance:
                cur_distance = max_distance
                count += 1
        
        return count
        



solution = Solution()
print(solution.jump([2,3,1,1,4]))