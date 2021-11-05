# -*- coding: utf-8 -*-
# @Date    : 2021-11-05 10:45:25
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        n, m = len(matrix), len(matrix[0])

        i, j = 0, m - 1

        while i < n and j >= 0:
            current = matrix[i][j]
            if current > target:
                j -= 1
            elif current < target:
                i += 1
            else:
                return True
        
        return False