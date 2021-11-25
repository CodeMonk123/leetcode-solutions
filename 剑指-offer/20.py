# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 16:48:23
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def is_integer(self, s:str)->bool:
        if s.startswith('+') or s.startswith('-'):
            s = s[1:]
        for ch in s:
            if not (ch>='0' and ch<='9'):
                return False
        return len(s) > 0

    def is_float(self, s:str)->bool:
        if s.startswith('+') or s.startswith('-'):
            s = s[1:]
        if '.' in s:
            if len(s) == 1:
                return False
            tokens = s.split('.')
            if len(tokens) > 2 or len(tokens) == 0:
                return False
            for token in tokens:
                for ch in token:
                    if not (ch>='0' and ch<='9'):
                        return False
            return True
        else:
            for ch in s:
                if not (ch>='0' and ch<='9'):
                    return False
            return len(s) > 0
        


    

    def isNumber(self, s: str) -> bool:
        s = s.strip(' ')
        s = s.replace('e', 'E')
        if 'E' in s:
            tokens = s.split('E')
            if len(tokens) != 2:
                return False
            part1 = tokens[0]
            part2 = tokens[1]
            if self.is_integer(part1) or self.is_float(part1):
                return self.is_integer(part2)
            return False
        else:
            return self.is_integer(s) or self.is_float(s)

solution = Solution()
test_cases1 = ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
for case in test_cases1:
    print(solution.isNumber(case))

test_cases2 = ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
for case in test_cases2:
    print(solution.isNumber(case))
