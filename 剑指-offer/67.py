# -*- coding: utf-8 -*-
# @Date    : 2021-11-07 16:06:25
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def strToInt(self, str: str) -> int:
        start = 0
        for idx, ch in enumerate(str):
            if ch != ' ':
                start = idx
                break
        if len(str) == 0:
            return 0
        
        if not(str[start] >= '0' and str[start] <= '9' or str[start] == '+' or str[start] == '-'):
            return 0

        res = 0
        int_max = (1 << 31)  - 1
        int_min = - (1<<31)
        sign = 1

        if str[start] == '-':
            sign = -1
            start += 1
        
        elif str[start] == '+':
            start += 1

        for i in range(start, len(str)):
            if str[i] >= '0' and str[i] <= '9':
                res *= 10
                res += (ord(str[i]) - ord('0'))
                if res * sign > int_max or res * sign < int_min:
                    break
            else:
                break
        
        res *= sign

        if res > int_max:
            return int_max
        elif res < int_min:
            return int_min
        
        return res

print(Solution().strToInt('2147483648'))