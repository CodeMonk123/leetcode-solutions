# -*- coding: utf-8 -*-
# @Date    : 2021-11-19 10:51:10
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def num_to_digits(self, n:int)->List[int]:
        res = []
        while n != 0:
            res.append(n % 10)
            n //= 10
        res.reverse()
        return res
    
    def digits_to_num(self, digits:List[int])->int:
        res = 0
        for digit in digits:
            res *= 10
            res += digit
        return res
        

    def _count(self, digits:List[int]) -> int:
        if len(digits) == 1:
            if digits[0] == 0:
                return 0
            return 1
        elif len(digits) == 2:
            part1 = digits[0] * 1
            part2 = self._count(digits[1:])
            if digits[0] > 1:
                part3 = 10
            elif digits[0] == 1:
                part3 = digits[1] + 1
            else:
                part3 = 0
                
            return part1 + part2 + part3
        else:
            part1 = digits[0] * self._count([9 for _ in range(len(digits)-1)])
            part2 = self._count(digits[1:])
            if digits[0] > 1:
                part3 = 10 ** (len(digits) - 1)
            elif digits[0] == 1:
                part3 = self.digits_to_num(digits[1:]) + 1
            else:
                part3 = 0
            

            return  part1 + part2 + part3

    def countDigitOne(self, n: int) -> int:
        digits = self.num_to_digits(n)
        return self._count(digits)

solution = Solution()
print(solution.countDigitOne(12)) # 5
print(solution.countDigitOne(13)) # 6
print(solution.countDigitOne(10)) # 2
print(solution.countDigitOne(100)) # 21
print(solution.countDigitOne(101)) # 23
print(solution.countDigitOne(102)) # 24
print(solution.countDigitOne(1000)) # 301
print(solution.countDigitOne(789))