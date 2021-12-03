# -*- coding: utf-8 -*-
# @Date    : 2021-12-01 10:05:25
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return
        for layer in range(n // 2):
            for i in range(n - 1 - layer * 2):
                x1, y1 = layer, i + layer
                x2, y2 = i + layer, n - 1 - layer
                x3, y3 = n-1-layer, n-1-layer-i
                x4, y4 = n-1-layer-i, layer
                matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4] = matrix[x4][y4],matrix[x1][y1], matrix[x2][y2], matrix[x3][y3]
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)
print(matrix)


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
print(matrix)