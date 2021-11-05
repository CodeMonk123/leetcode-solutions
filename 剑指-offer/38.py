# -*- coding: utf-8 -*-
# @Date    : 2021-11-05 09:41:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def __init__(self) -> None:
        self.ans = set()
        self.used = []
    
    def find_next(self, s:str, current:str):
        if len(current) == len(s):
            self.ans.add(current)
            return
        
        for idx, ch in enumerate(s):
            if not self.used[idx]:
                candidate = copy.deepcopy(current) + ch
                self.used[idx] = True
                self.find_next(s, candidate)
                self.used[idx] = False

    def permutation(self, s: str) -> List[str]:
        self.ans = set()
        self.used = [False for _ in s]
        self.find_next(s, '')
        return list(self.ans)

solution = Solution()
print(solution.permutation('abc'))