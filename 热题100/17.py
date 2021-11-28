# -*- coding: utf-8 -*-
# @Date    : 2021-11-28 15:03:16
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def __init__(self) -> None:
        self.digit_to_alphabet = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv' ,
            '9' : 'wxyz',
        }

    def dfs(self, digits:str, start:int, current:str, res:List[str]):
        if start == len(digits):
            res.append(current)
            return
        
        for ch in self.digit_to_alphabet[digits[start]]:
            self.dfs(digits, start + 1, current + ch, res)

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) > 0:
            self.dfs(digits, 0, '', res)
        return res
        
print(Solution().letterCombinations('23'))