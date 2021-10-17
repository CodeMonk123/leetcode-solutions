# -*- coding: utf-8 -*-
# @Date    : 2021-10-17 15:37:50
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def numTrees(self, n: int) -> int:
        res = [0 for _ in range(n+1)]
        res[0] = 1
        res[1] = 1
        for num_nodes in range(2, n+1):
            for left_nodes in range(0, n):
                res[num_nodes] += res[left_nodes] * res[num_nodes - 1 - left_nodes]

        return res[n]

solution = Solution()
print(solution.numTrees(3))