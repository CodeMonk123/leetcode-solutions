# -*- coding: utf-8 -*-
# @Date    : 2021-11-26 16:39:40
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        ch_to_index= {}
        start = 0
        for i, ch in enumerate(s):
            if ch not in ch_to_index:
                ch_to_index[ch] = i
                max_length = max(max_length, i + 1 - start)
            else:
                new_start = ch_to_index[ch] + 1
                for j in range(start, new_start):
                    ch_to_index.pop(s[j])
                start = new_start
                ch_to_index[ch] = i

        
        return max_length