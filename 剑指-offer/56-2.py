# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 10:35:24
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for num in count:
            if count[num] == 1:
                return num
        
        