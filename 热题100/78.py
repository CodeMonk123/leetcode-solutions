# -*- coding: utf-8 -*-
# @Date    : 2021-12-05 20:37:29
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def dfs(self, nums:List[int], start:int, current:List[int], res:List[List[int]]):
        if start == len(nums):
            res.append(current)
            return
        self.dfs(nums, start+1, current, res)
        self.dfs(nums, start+1, current + [nums[start]], res)
        

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res