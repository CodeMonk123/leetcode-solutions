# -*- coding: utf-8 -*-
# @Date    : 2021-10-17 15:42:29
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target_sum = int(total_sum / 2)
        if max(nums) > target_sum:
            return False

        dp = [
            [False for _ in range(target_sum + 1)] for _ in range(len(nums) + 1)
        ]

        dp[0][0] = True
        for i in range(1, 1 + len(nums)):
            for j in range(target_sum + 1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]


        return dp[len(nums) - 1][target_sum]

solution = Solution()
print(solution.canPartition([1,5,5,11]))
print(solution.canPartition([1,2,3,4]))
print(solution.canPartition([1,2,3,5]))