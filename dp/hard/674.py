# -*- coding: utf-8 -*-
# @Date    : 2021-11-01 10:58:13
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for k in range(1, n):
            for i in range(n-k):
                # dp[i][i+k]
                if s[i] == s[i+k]:
                    if k == 1:
                        dp[i][i+k] = 1
                    else:
                        dp[i][i+k] = dp[i+1][i+k-1]
                else:
                    dp[i][i+k] = 0
        
        return sum([sum(x) for x in dp])
        
solution = Solution()
print(solution.countSubstrings("aaa"))
print(solution.countSubstrings("abc"))
                