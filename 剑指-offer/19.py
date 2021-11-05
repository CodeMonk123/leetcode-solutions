# -*- coding: utf-8 -*-
# @Date    : 2021-11-02 10:10:49
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_s = '&' + s + '&'
        new_p = '&' + p + '&'
        m,n = len(new_s), len(new_p)

        matched = [[False for _ in range(n)] for _ in range(m)]

        if new_s[0] == new_p[0] or new_p[0] == '.':
            matched[0][0] = True
        
        for i in range(1, m):
            matched[i][0] = False
        

        for i in range(m):
            for j in range(1,n):
                if new_s[i] == new_p[j] or new_p[j] == '.':
                    if i > 0 and j > 0:
                        matched[i][j] = matched[i-1][j-1]

                    
                elif j > 0 and new_p[j] == '*':
                   matched[i][j] = matched[i][j-1]
                   matched[i][j] = matched[i][j] or (i==0 and j == 1) or(j>=2 and matched[i][j-2])
                   matched[i][j] = matched[i][j] or (i > 0 and matched[i-1][j] and (new_s[i]==new_p[j-1] or new_p[j-1]=='.'))

        # for x in matched:
        #     print(x)

        return matched[-1][-1]

solution = Solution()

print(solution.isMatch("aa", "a"))
print(solution.isMatch("aa", "a*"))
print(solution.isMatch("ab", ".*"))
print(solution.isMatch("aaa", "ab*ac*a"))
print(solution.isMatch("aab", "c*a*b"))
print(solution.isMatch("aa", "ab*"))
print(solution.isMatch('a', '.*.'))