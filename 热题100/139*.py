# -*- coding: utf-8 -*-
# @Date    : 2021-12-08 10:40:33
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        available_start = set([0])
        wordDict = set(wordDict)
        for i in range(1, len(s)+1):
            temp = set()
            for start in available_start:
                if s[start:i] in wordDict:
                    temp.add(i)
            available_start = available_start.union(temp)
        return len(s) in available_start

solution = Solution()
print(solution.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))