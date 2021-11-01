# -*- coding: utf-8 -*-
# @Date    : 2021-10-29 14:53:10
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in text2] for _ in text1]

        for i in range(len(text2)):
            if text2[i] == text1[0]:
                for j in range(i, len(text2)):
                    dp[0][j] = 1
                break   
        
        for i in range(len(text1)):
            if text1[i] == text2[0]:
                for j in range(i, len(text1)):
                    dp[j][0] = 1
                break
        
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + (1 if text1[i]==text2[j] else 0))
        # print(dp)
        res = max([max(x) for x in dp])
        return res

solution = Solution()
print(solution.longestCommonSubsequence('abcde', 'ace'))