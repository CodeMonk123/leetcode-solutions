# -*- coding: utf-8 -*-
# @Date    : 2021-11-01 10:25:45
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def _max_common_sub_sequence(self, word1:str, word2:str)->int:
        dp = [[0 for _ in word2] for _ in word1]
        for i in range(len(word1)):
            if word1[i] == word2[0]:
                for j in range(i, len(word1)):
                    dp[j][0] = 1
                break
        
        for i in range(len(word2)):
            if word2[i] == word1[0]:
                for j in range(i, len(word2)):
                    dp[0][j] = 1
                break
        
        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        total_length = len(word1) + len(word2)
        return total_length - 2 * self._max_common_sub_sequence(word1, word2)

solution = Solution()
print(solution.minDistance("sea", "eat"))