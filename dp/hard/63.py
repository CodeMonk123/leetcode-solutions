# -*- coding: utf-8 -*-
# @Date    : 2021-10-15 14:29:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths = [[0 for _ in obstacleGrid[0]] for _ in obstacleGrid]
        paths[0][0] = 1 - obstacleGrid[0][0]
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        reachable = (paths[0][0] == 1) 
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                paths[i][0] = 0
                reachable = False
            elif reachable:
                paths[i][0] = 1
            else:
                paths[i][0] = 0
        
        reachable = (paths[0][0] == 1) 
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                paths[0][i] = 0
                reachable = False
            elif reachable:
                paths[0][i] = 1
            else:
                paths[0][i] = 0

        print(paths)

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i-1][j] * (1 - obstacleGrid[i-1][j]) + paths[i][j-1] * (1 - obstacleGrid[i][j-1])
        print(paths)
        return paths[-1][-1]

solution = Solution()
print(solution.uniquePathsWithObstacles([[0,0], [1,1], [0,0]]))