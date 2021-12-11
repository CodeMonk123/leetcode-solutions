# -*- coding: utf-8 -*-
# @Date    : 2021-12-10 11:35:45
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0 for _ in nums] for _ in range(2)]
        dp[0][0] = nums[0]
        dp[1][0] = 0
        for i in range(1, len(nums)):
            dp[0][i] = nums[i] + dp[1][i-1]
            dp[1][i] = max(dp[1][i-1], dp[0][i-1])
        
        return max(max(dp[1]), max(dp[0]))

solution = Solution()
print(solution.rob([1,2,3,1]))
print(solution.rob([2,7,9,3,1]))