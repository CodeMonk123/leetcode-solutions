# -*- coding: utf-8 -*-
# @Date    : 2021-12-10 11:28:15
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if num == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = num
                    count = 1
        return candidate

solution = Solution()
print(solution.majorityElement([3,2,3]))
print(solution.majorityElement([10, 9,9,9,10]))