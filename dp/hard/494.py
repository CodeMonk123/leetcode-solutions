# -*- coding: utf-8 -*-
# @Date    : 2021-10-19 20:27:38
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0 
        total = sum(nums)
        if total < target or total < -target:
            return 0

        dp = [{val:0 for val in range(-total, total+1)} for _ in nums]

        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        for i in range(1, len(nums)):
            for v in range(-total, total + 1):
                # dp[i][v] = dp[i-1][v+nums[i]] + dp[i-1][v-nums[i]]
                if v + nums[i] <= total:
                    dp[i][v] += dp[i-1][v+nums[i]]
                if v - nums[i] >= -total:
                    dp[i][v] += dp[i-1][v-nums[i]]
        # print(dp)
        return dp[-1][target]

solution = Solution()
print(solution.findTargetSumWays(nums = [1,1,1,1,1], target = 3))
print(solution.findTargetSumWays([0,0,0,0,1], 1))      

