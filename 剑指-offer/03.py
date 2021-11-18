# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 11:20:51
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        exist_nums = set()
        for num in nums:
            if num in exist_nums:
                return num
            exist_nums.add(num)