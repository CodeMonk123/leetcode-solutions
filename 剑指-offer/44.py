# -*- coding: utf-8 -*-
# @Date    : 2021-11-22 16:10:20
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        
        x = 2
        n -= 10
        while n - x * 9 * (10 ** (x-1)) > 0:
            n -= x * 9 * (10 ** (x-1)) 
            x+=1
        # print('n = {}'.format(n))
        start = int(10 ** (x-1)) + n // x
        # print(start)
        return int(str(start)[n % x])

solution = Solution()
# print(solution.findNthDigit(11))
# print(solution.findNthDigit(12))        
# print(solution.findNthDigit(13)) 
# print(solution.findNthDigit(14)) 
# print(solution.findNthDigit(15)) 
print(solution.findNthDigit(1000))