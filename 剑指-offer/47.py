# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 11:31:38
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        max_values = [[0 for _ in range(n)] for _ in range(m)]
        max_values[m-1][n-1] = grid[m-1][n-1]
        for i in range(n-2, -1, -1):
            max_values[m-1][i] = max_values[m-1][i+1] + grid[m-1][i]
        
        for i in range(m-2, -1, -1):
            max_values[i][n-1] = max_values[i+1][n-1] + grid[i][n-1]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                max_values[i][j] = grid[i][j] + max(max_values[i][j+1], max_values[i+1][j])
        
        return max_values[0][0]
