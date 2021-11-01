# -*- coding: utf-8 -*-
# @Date    : 2021-10-29 15:02:14
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            if nums1[i] == nums2[0]:
                for j in range(i, m):    
                    dp[j][0] = 1
                break
            
        
        for i in range(n):
            if nums2[i] == nums1[0]:
                for j in range(i, n):
                    dp[0][j] = 1
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i] == nums2[j]:
                        dp[i][j] = max(1 + dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

        # print(dp)
        return max([max(x) for x in dp ])

solution = Solution()
print(solution.maxUncrossedLines(nums1 = [1,4,2], nums2 = [1,2,4]))
print(solution.maxUncrossedLines(nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]))
print(solution.maxUncrossedLines(nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]))
