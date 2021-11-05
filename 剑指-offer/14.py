# -*- coding: utf-8 -*-
# @Date    : 2021-11-04 14:06:01
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def cuttingRope(self, n: int) -> int:
            max_prod = [0 for _ in range(n+1)]
            max_prod[1] = 1
            max_prod[2] = 1
            for i in range(3, n+1):
                for j in range(1, i // 2+1):
                    max_prod[i] = max(max_prod[i], max(j,max_prod[j]) * max(i-j,max_prod[i-j]))
            # print(max_prod)
            return max_prod[n]
    

solution = Solution()
print(solution.cuttingRope(10))