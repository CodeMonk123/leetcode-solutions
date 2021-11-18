# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 11:18:18
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        fib1, fib2 = 1, 1
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
        
        return fib2 % (int(1e9 + 7))

solution = Solution()
print(solution.fib(5))