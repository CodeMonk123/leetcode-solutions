# -*- coding: utf-8 -*-
# @Date    : 2021-12-01 10:33:00
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def _generate_key(self, s:str)->str:
        count = [0 for _ in range(26)]
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        return ','.join(map(str, count))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            k = self._generate_key(s)
            if k not in groups:
                groups[k] = [s]
            else:
                groups[k].append(s)
        
        return list(groups.values())

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))