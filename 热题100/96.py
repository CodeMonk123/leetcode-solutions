# -*- coding: utf-8 -*-
# @Date    : 2021-12-06 10:38:35
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.initialized = False

    def numTrees(self, n: int) -> int:
        if not self.initialized:
            self.initialized = True
            self.ans = [-1 for _ in range(n+1)]
        
        if self.ans[n] != -1:
            return self.ans[n]


        if n <= 2:
            self.ans[n] = n
            self.ans[0] = 1
            return n

        res = 0
        for i in range(1, n+1):
            res += self.numTrees(n - i) * self.numTrees(i - 1)
        self.ans[n] = res
        return res

print(Solution().numTrees(3))