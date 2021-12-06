# -*- coding: utf-8 -*-
# @Date    : 2021-12-05 21:34:49
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0
        left = [-1 for _ in heights]
        right = [-1 for _ in heights]
        for idx, height in enumerate(heights):
            if len(s) == 0 or s[-1][0] <=  height:
                s.append((height, idx))
            else:
                while True:
                    if len(s) == 0:
                        s.append((height, idx))
                        break
                    elif s[-1][0] > height:
                        right[s[-1][1]] = idx
                        s.pop()
                    else:
                        s.append((height, idx))
                        break
        s = []

        for idx in range(len(heights)-1, -1, -1):
            height = heights[idx]
            if len(s) == 0 or s[-1][0] <=  height:
                s.append((height, idx))
            else:
                while True:
                    if len(s) == 0:
                        s.append((height, idx))
                        break
                    elif s[-1][0] > height:
                        left[s[-1][1]] = idx
                        s.pop()
                    else:
                        s.append((height, idx))
                        break
        print(left)
        print(right)

        for idx in range(len(heights)):
            if right[idx] == -1:
                right[idx] = len(heights) 
            area = heights[idx] * (right[idx] - left[idx] - 1)
            max_area = max(max_area, area)
        return max_area


solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))
print(solution.largestRectangleArea([0,1,0,2,1,0,1,3,2,1,2,1]))
