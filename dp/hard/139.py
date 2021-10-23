# -*- coding: utf-8 -*-
# @Date    : 2021-10-23 15:36:36
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        available = set([0])
        for i in range(len(s)+1):
            is_validate= False
            for start in available:
                # print('{} in word set is {}'.format(s[start:i], s[start:i] in word_set))
                if s[start:i] in word_set:
                    is_validate = True
            if is_validate:
                available.add(i)
        
        return len(s) in available


solution = Solution()
print(solution.wordBreak('applepenapple', ['apple', 'pen']))