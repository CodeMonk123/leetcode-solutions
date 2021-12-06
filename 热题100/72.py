# -*- coding: utf-8 -*-
# @Date    : 2021-12-03 14:33:07
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[i-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
    