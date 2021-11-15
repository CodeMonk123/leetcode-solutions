# -*- coding: utf-8 -*-
# @Date    : 2021-11-15 10:47:28
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        space = 6 ** n
        dp = [[0 for _ in range(6*n + 1)] for _ in range(n)]
        for i in range(1, 7):
            dp[0][i] = 1 / 6
        
        for i in range(1, n):
            for j in range(i+1, 1 + 6 * (i+1)):
                for k in range(1,7):
                    dp[i][j] += 1/6 * dp[i-1][j-k]

        return dp[-1][n:6*n+1]

solution = Solution()
print(solution.dicesProbability(1))
print(solution.dicesProbability(2))
print(solution.dicesProbability(9))