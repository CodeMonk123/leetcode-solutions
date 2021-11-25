# -*- coding: utf-8 -*-
# @Date    : 2021-11-22 17:06:18
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy
import functools

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        temp = functools.reduce(lambda x,y: x^y, nums)
        mask = 0x1
        while temp & 0x1 != 1:
            mask <<= 1
            temp >>= 1
        first,second = 0, 0
        for num in nums:
            if num & mask > 0:
                first ^= num
            else:
                second ^= num
        
        return [first, second]
    
solution = Solution()
print(solution.singleNumbers([4,1,4,6]))
        