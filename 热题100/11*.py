# -*- coding: utf-8 -*-
# @Date    : 2021-11-28 10:10:34
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = (right - left) * min(height[right], height[left])
        while left < right:
            if height[right] <= height[left]:
                right -= 1
                max_area = max(max_area, (right - left) * min(height[right], height[left]))
            else:
                left += 1
                max_area = max(max_area, (right - left) * min(height[right], height[left]))
        
        return max_area


solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
