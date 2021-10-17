# -*- coding: utf-8 -*-
# @Date    : 2021-10-17 15:27:50
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def integerBreak(self, n: int) -> int:

        res = [0 for _ in range(n+1)]
        res[2] = 1
        res[1] = 1
        for i in range(3,n+1):
            for j in range(1, int(i/2)+1):
                res[i] = max(res[i], max(j,res[j]) * max(i-j,res[i-j]))
        
        return res[n]

solution = Solution()

print(solution.integerBreak(2))
print(solution.integerBreak(3))
print(solution.integerBreak(4))
print(solution.integerBreak(10))
