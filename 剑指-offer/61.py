# -*- coding: utf-8 -*-
# @Date    : 2021-11-05 10:18:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        count_0 = 0
        min_num = 14
        max_num = 0
        record = set()

        for num in nums:
            if num == 0:
                count_0 += 1
            else:
                if num in record:
                    return False
                record.add(num)
                if num < min_num:
                    min_num = num
                if num > max_num:
                     max_num = num
        
        if count_0 >= 4:
            return True

        return  max_num - min_num < 5