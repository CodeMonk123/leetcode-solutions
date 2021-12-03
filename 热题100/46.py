# -*- coding: utf-8 -*-
# @Date    : 2021-12-01 09:59:44
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def dfs(self, nums:List[int], used:List[bool], current:List[int], res:List[List[int]]):
        if len(current) == len(nums):
            res.append(current)
            return
        
        for i, num in enumerate(nums):
            if not used[i]:
                used[i] = True
                self.dfs(nums, used, current + [num], res)
                used[i] = False
        

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False for _ in nums]
        self.dfs(nums, used, [], res)
        return res

solution = Solution()
print(solution.permute([1,2,3]))