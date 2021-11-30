# -*- coding: utf-8 -*-
# @Date    : 2021-11-30 10:26:24
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        max_length = [0 for _ in range(n)]

        for i in range(n):
            if s[i] == '(':
                max_length[i] = 0
            elif s[i] == ')':
                if i > 0 and s[i-1] == '(':
                    max_length[i] = 2 + (0 if i==1 else max_length[i-2])
                elif i > 0 and s[i-1] == ')':
                    index = i - 1 - max_length[i-1] 
                    if index >= 0 and s[index] == '(':
                        max_length[i] = 2 + max_length[i-1] + (0 if index==0 else max_length[index-1])
        
        return max(max_length)



solution = Solution()

print(solution.longestValidParentheses(')()())'))
print(solution.longestValidParentheses('()()'))
print(solution.longestValidParentheses("()(())"))