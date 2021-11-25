# -*- coding: utf-8 -*-
# @Date    : 2021-11-22 15:54:05
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > n // 2:
                return num
        