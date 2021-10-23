# -*- coding: utf-8 -*-
# @Date    : 2021-10-20 11:14:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = [0 for _ in range(amount + 1)]
        count[0] = 1

        for coin in coins:
            
            for val in range(coin, amount + 1):
                count[val] += count[val - coin]
        
        return count[amount]

solution = Solution()

print(solution.change(5, [1,2,5]))
print(solution.change(3, [2]))
print(solution.change(0, [7]))