# -*- coding: utf-8 -*-
# @Date    : 2021-11-17 11:17:23
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        ways_1 = 1
        ways_2 = 2
        for i in range(n-2):
            temp = ways_1 + ways_2
            ways_1 = ways_2
            ways_2 = temp
        
        return ways_2 % int(1e9 + 7)

solution = Solution()
print(solution.numWays(2))
print(solution.numWays(7))