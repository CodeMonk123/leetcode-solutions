# -*- coding: utf-8 -*-
# @Date    : 2021-11-30 11:18:15
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def dfs(self, candidates:List[int], start:int, target:int, current:List[int], res:List[List[int]]):
        if target == 0:
            res.append(current)
        if start >= len(candidates):
            return
        if candidates[start] > target:
            return
        else:
            for i in range(target // candidates[start]):
                current_copy = copy.deepcopy(current)
                current_copy += [candidates[start]] * (i+1)
                self.dfs(candidates, start+1, target - (i+1) * candidates[start], current_copy, res)
            self.dfs(candidates, start+1, target, current, res)
                


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res

solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))
print(solution.combinationSum([2,3,5], 8))