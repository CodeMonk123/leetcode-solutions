# -*- coding: utf-8 -*-
# @Date    : 2021-11-10 10:07:11
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def validate(self, x:int, y:int, k:int)->bool:
        digit_sum = 0
        while x != 0:
            digit_sum += x % 10
            x //= 10
        while y != 0:
            digit_sum += y % 10
            y //= 10
        return digit_sum <= k

    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        candidates = set()
        visited.add((0,0))
        if m > 1:
            candidates.add((1,0))
        if n > 1:
            candidates.add((0,1))

        while len(candidates) > 0:
            (x, y) = candidates.pop()
            if not self.validate(x,y,k):
                continue
            visited.add((x,y))
            # print('visit {}'.format((x,y)))
            new_candidates = []
            if x > 0:
                new_candidates.append((x-1, y))
            if x < m-1:
                new_candidates.append((x+1, y))
            if y > 0:
                new_candidates.append((x, y-1))
            if y < n-1:
                new_candidates.append((x, y+1))
            for candidate in new_candidates:
                if candidate not in visited:
                    candidates.add(candidate)
        
        return len(visited)

solution = Solution()
print(solution.movingCount(3,1,0))
