# -*- coding: utf-8 -*-
# @Date    : 2021-10-15 14:05:45
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        
        method1, method2 = 1, 1
        for i in range(1, n):
            method = method1 + method2
            method1, method2 = method2, method
        return method


solution = Solution()
print(solution.climbStairs(3))