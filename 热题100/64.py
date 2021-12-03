# -*- coding: utf-8 -*-
# @Date    : 2021-12-03 14:24:55
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        if m == 1:
            return sum(grid[0])
        if n == 1:
            return sum([x[0] for x in grid])
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1:
                    if j != n-1:
                        grid[i][j] += grid[i][j+1]
                elif j == n-1:
                    if i != m-1:
                        grid[i][j] += grid[i+1][j]
                else:
                    grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        
        return grid[0][0]