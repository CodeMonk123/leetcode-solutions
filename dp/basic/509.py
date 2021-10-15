# -*- coding: utf-8 -*-
# @Date    : 2021-10-15 13:47:48
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy
from functools import lru_cache


class Solution:
    @lru_cache
    def _fib(self, n:int)->int:    
        if n <= 2:
            return 1
        return self._fib(n-1) + self._fib(n-2)

    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n <= 2:
            return 1
        fib1, fib2 = 1, 1
        for i in range(n-2):
            fib3 = fib1 + fib2
            fib1, fib2 = fib2, fib3
        return fib2

solution = Solution()
import time
start_time = time.time()
print(solution.fib(50))
print(time.time() - start_time)

start_time = time.time()
print(solution._fib(50))
print(time.time() - start_time)