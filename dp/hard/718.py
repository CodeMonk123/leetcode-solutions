# -*- coding: utf-8 -*-
# @Date    : 2021-10-29 14:34:19
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in nums2] for _ in nums1]
        
        for i in range(0, len(nums2)):
            if nums2[i] == nums1[0]:
                dp[0][i] = 1
        
        for i in range(0, len(nums1)):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1

        
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                dp[i][j] = (dp[i-1][j-1] + 1) if nums1[i] == nums2[j] else 0
        

        res = max([max(x) for x in dp])
        return res        
