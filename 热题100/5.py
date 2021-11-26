# -*- coding: utf-8 -*-
# @Date    : 2021-11-26 17:00:32
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1 
        res = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        
        for k in range(2, len(s) + 1):
            for i in range(0, len(s) - k + 1):
                if s[i] != s[i+k-1]:
                    continue
                else:
                    if k == 2 or dp[i+1][i+k-2]:
                        dp[i][i+k-1] = True
                        max_length = max(max_length, k)
                        res = s[i:i+k]
        return res
    
solution = Solution()
print(solution.longestPalindrome('babad'))
print(solution.longestPalindrome('cbbd'))
print(solution.longestPalindrome('a'))
print(solution.longestPalindrome('ac'))