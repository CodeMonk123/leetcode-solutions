# -*- coding: utf-8 -*-
# @Date    : 2021-11-28 10:15:26
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = '&' + s + '#'
        p = '&' + p + '#'
        m,n = len(s), len(p)
        dp = [[False for _ in range(m)] for _ in range(n)]
        dp[0][0] = True
        for i in range(2, n):
            if p[i] == '*':
                dp[i][0] = dp[i-2][0]
                
        for i in range(1, n):
            for j in range(1, m):
                if p[i] != '.' and p[i] != '*':
                    if p[i] == s[j]:
                        dp[i][j] = dp[i-1][j-1]
                elif p[i] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i] == '*':
                    dp[i][j] = dp[i-2][j] # 0个
                    dp[i][j] = dp[i][j] or dp[i-1][j] #1个
                    dp[i][j] = dp[i][j] or (dp[i][j-1] and (p[i-1]=='.' or s[j]==p[i-1])) #多个
                
        
        return dp[-1][-1]

solution = Solution()
print(solution.isMatch(s="aa", p="a"))
print(solution.isMatch('aa', 'a*'))
print(solution.isMatch('ab', '.*'))
print(solution.isMatch('aab', 'c*a*b'))
print(solution.isMatch('aaa', '.*'))
print(solution.isMatch('aaa', 'ab*a'))