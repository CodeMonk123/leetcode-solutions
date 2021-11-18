# -*- coding: utf-8 -*-
# @Date    : 2021-11-15 16:38:55
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b = [1 for _ in a]
        if len(a) < 2:
            return b
        
        prod1 = 1
        for i in range(len(a)-1, 0, -1):
            prod1 *= a[i]
            b[i-1] = prod1
        
        prod2 = 1
        for i in range(0, len(a)-1):
            prod2 *= a[i]
            b[i+1] *= prod2
        
        return b

solution = Solution()
print(solution.constructArr([1,2,3,4,5]))