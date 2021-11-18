# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 10:51:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        index = {}
        start = 0
        max_length = 1
        index[s[0]] = 0
        for i in range(1, len(s)):
            if s[i] not in index:
                index[s[i]] = i
                max_length = max(max_length, i + 1 - start)
            else:
                new_start = index[s[i]] + 1
                for j in range(start, new_start):
                    index.pop(s[j])
                index[s[i]] = i
                start = new_start


        return max_length

solution = Solution()
print(solution.lengthOfLongestSubstring('abcabcbb'))
print(solution.lengthOfLongestSubstring("tmmzuxt")) 
print(solution.lengthOfLongestSubstring('pwwkew'))         
        
