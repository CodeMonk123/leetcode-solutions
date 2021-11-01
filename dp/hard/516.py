# -*- coding: utf-8 -*-
# @Date    : 2021-11-01 11:07:43
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        

        for k in range(1, n):
            for i in range(n-k):
                if s[i] == s[i+k]:
                    if k == 1:
                        dp[i][i+k] = 2
                    else:
                        dp[i][i+k] = 2 + dp[i+1][i+k-1]
                else:
                    dp[i][i+k] = max(dp[i+1][i+k], dp[i][i+k-1])
        
        

        return dp[0][-1]

solution = Solution()
print(solution.longestPalindromeSubseq("bbbab"))
print(solution.longestPalindromeSubseq("cbbd"))