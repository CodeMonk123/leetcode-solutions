# -*- coding: utf-8 -*-
# @Date    : 2021-11-11 16:05:42
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        start = 1
        res = []
        while start <= target // 2:
            end = start + 1
            while True:
                partial_sum = ((start + end) * (end + 1 - start)) // 2
                if partial_sum < target:
                    end += 1
                elif partial_sum == target:
                    res.append([x for x in range(start, end+1)])
                    start += 1
                    break
                else:
                    start += 1
                    break
        return res

solution = Solution()
print(solution.findContinuousSequence(15))