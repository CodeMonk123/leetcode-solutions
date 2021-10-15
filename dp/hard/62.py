# -*- coding: utf-8 -*-
# @Date    : 2021-10-15 14:22:14
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]
        paths[0][0] = 1
        for i in range(n):
            paths[0][i] = 1
        for j in range(m):
            paths[j][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i][j-1] + paths[i-1][j]
        
        return paths[-1][-1]