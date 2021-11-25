# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 16:15:57
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def sumNums(self, n: int) -> int:
        
        return sum(range(n+1))

solution = Solution()
print(solution.sumNums(9))