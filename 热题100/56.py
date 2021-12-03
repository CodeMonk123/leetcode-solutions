# -*- coding: utf-8 -*-
# @Date    : 2021-12-01 11:03:10
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: tuple(x))
        res = []
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
            else:
                if res[-1][1] >= interval[0]:
                    top = res.pop()
                    res.append([top[0], max(top[1], interval[1])])
                else:
                    res.append(interval)
        
        return res

solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
print(solution.merge([[1,3],[3,6],[8,10],[15,18]]))