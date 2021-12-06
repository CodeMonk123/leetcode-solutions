# -*- coding: utf-8 -*-
# @Date    : 2021-12-06 09:57:25
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def max_area(self, heights:List[int])->int:
        s = []
        left = [-1 for _ in heights]
        right = [-1 for _ in heights]
        for i in range(len(heights)):
            height = heights[i]
            if len(s) == 0 or s[-1][0] <= height:
                s.append((height,i))
            else:
                while True:
                    if len(s) == 0:
                        s.append((height,i))
                        break
                    elif s[-1][0] > height:
                        right[s[-1][1]] = i
                        s.pop()
                    else:
                        s.append((height,i))
                        break
        
        for i in range(len(heights)-1, -1, -1):
            height = heights[i]
            if len(s) == 0 or s[-1][0] <= height:
                s.append((height,i))
            else:
                while True:
                    if len(s) == 0:
                        s.append((height,i))
                        break
                    elif s[-1][0] > height:
                        left[s[-1][1]] = i
                        s.pop()
                    else:
                        s.append((height,i))
                        break
                        
        ans = 0
        for i in range(len(heights)):
            if right[i] == -1:
                right[i] = len(heights)
            area = heights[i] * (right[i] - left[i] - 1)
            ans = max(ans, area)
        
        return ans




    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        left = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            count = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    count += 1
                    left[i][j] = count
                else:
                    count = 0
        
        max_area = 0
        for j in range(n):
            column = [left[i][j] for i in range(m)]
            max_area = max(max_area, self.max_area(column))

        return max_area

solution = Solution()
print(solution.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))