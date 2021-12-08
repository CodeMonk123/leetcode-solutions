# -*- coding: utf-8 -*-
# @Date    : 2021-12-08 10:28:30
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                start = num + 1
                while start in nums:
                    length += 1
                    start += 1
                max_length = max(max_length, length)
        return max_length