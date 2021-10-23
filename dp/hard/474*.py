# -*- coding: utf-8 -*-
# @Date    : 2021-10-20 10:56:36
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def _count(self, s:str)->Tuple[int,int]:
        # '0001111' -> (3,4)
        count_0, count_1 = 0, 0
        for ch in s:
            if ch == '0':
                count_0 += 1
            else:
                count_1 += 1
        return count_0, count_1

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = list(map(self._count, strs))
        counts = sorted(counts, key=lambda x: x[0] + x[1])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for count in counts:
            for i in range(m, count[0] - 1, -1):
                for j in range(n, count[1] - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - count[0]][j-count[1]])
        
        return dp[m][n]

solution = Solution()
print(solution.findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))