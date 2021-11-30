# -*- coding: utf-8 -*-
# @Date    : 2021-11-30 12:57:24
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = 0
        max_index = 0
        res = 0
        for i,h in enumerate(height):
            if h > max_height:
                max_height = h
                max_index = i
        
        current_max_height = height[0]
        for i in range(1,max_index):
            if height[i] > current_max_height:
                current_max_height = height[i]
            else:
                res += (current_max_height - height[i])
        
        current_max_height = height[-1]
        for i in range(len(height)-2, max_index, -1):
            if height[i] > current_max_height:
                current_max_height = height[i]
            else:
                res += (current_max_height - height[i])
        
        return res

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trap([4,2,0,3,2,5]))