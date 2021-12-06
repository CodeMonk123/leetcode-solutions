# -*- coding: utf-8 -*-
# @Date    : 2021-12-05 20:31:57
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        for ch in t:
            target[ch] = 1 + target.get(ch, 0) 
        
        min_left, min_right = 0, 0
        min_length = len(s) + 1
        
        def validate(d)->bool:
            for _, v in d.items():
                if v > 0:
                    return False
            return True
        
        right, left = 0, 0
        while right < len(s):
            if s[right] in target:
                target[s[right]] -= 1
            while validate(target):
                if right + 1 - left < min_length:
                    min_left, min_right = left, right
                    min_length = right + 1 - left
                if s[left] in target:
                    target[s[left]] += 1
                left += 1
                
            right += 1
        
        return s[min_left:min_right+1] if min_length <= len(s) else ''