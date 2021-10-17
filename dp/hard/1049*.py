# -*- coding: utf-8 -*-
# @Date    : 2021-10-17 16:03:50
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        total = sum(stones)
        target = int(total / 2)
        print(total, target)
        dp = [False for _ in range(target + 1)]

        dp[0] = True
        for stone in stones:
            new_targets = []
            for i in range(target + 1):
                if dp[i]:
                    if i+stone <= target:
                        new_targets.append(i + stone)
                        print('{} + {} = {}'.format(i, stone, i+stone))

            for t in new_targets:
                dp[t] = True

        max_partial_sum = 0
        for i in range(target + 1):
            if dp[i]:
                max_partial_sum = i

        return total - 2 * max_partial_sum

solution = Solution()
# print(solution.lastStoneWeightII([2,7,4,1,8,1])) 
# print(solution.lastStoneWeightII([31,26,33,21,40]))
# print(solution.lastStoneWeightII([53,54,3,61,67]))
print(solution.lastStoneWeightII([21,60,61,20,31]))