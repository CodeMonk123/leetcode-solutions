# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 10:25:53
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def fast_pow(self, x:float, n:int) -> float:
        temp = x
        res = 1.0
        while n != 0:
            if n & 0x1 == 1:
                res *= temp
            n >>= 1
            temp *= temp
        return res

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n > 0:
            return self.fast_pow(x, n)
            
        elif n < 0:
            return 1.0 / self.fast_pow(x, int(-n))

solution = Solution()
print(solution.myPow(2, 10))
print(solution.myPow(2.1, 3))
print(solution.myPow(2.0, -2147483648))