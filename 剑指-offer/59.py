# -*- coding: utf-8 -*-
# @Date    : 2021-11-07 15:43:19
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]
        
        h = [(-x, idx) for (idx, x) in enumerate(nums[:k-1])]
        heapq.heapify(h)
        res = []

        for i in range(k-1, len(nums)):
            heapq.heappush(h, (-nums[i], i))
            while h[0][1] < i + 1 - k:
                heapq.heappop(h)
            x, _ = h[0]
            res.append(-x)
        

        return res
    
solution = Solution()
print(solution.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
        

