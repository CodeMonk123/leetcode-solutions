# -*- coding: utf-8 -*-
# @Date    : 2021-10-23 15:18:35
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy
import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [1e5 for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            for j in range(i*i, n+1):
                dp[j] = min(dp[j], 1 + dp[j - i*i])
        
        return dp[n]

solution = Solution()
print(solution.numSquares(12))
print(solution.numSquares(13))