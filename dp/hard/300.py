# -*- coding: utf-8 -*-
# @Date    : 2021-10-29 14:27:10
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_sub_sequence = [1 for _ in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    max_sub_sequence[i] = max(max_sub_sequence[i], 1+ max_sub_sequence[j])
        return max(max_sub_sequence)