# -*- coding: utf-8 -*-
# @Date    : 2021-11-29 10:40:31
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def dfs(self, current:str, n:int, left_count:int, right_count:int,res:List[str]):
        if len(current) == 2 * n:
            res.append(current)
            return
        
        if left_count < n:
            self.dfs(current + '(', n, left_count + 1, right_count, res)
        
        if right_count < left_count:
            self.dfs(current + ')', n, left_count, right_count + 1, res)
        

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs('', n, 0, 0, res)
        return res


solution = Solution()
print(solution.generateParenthesis(3))