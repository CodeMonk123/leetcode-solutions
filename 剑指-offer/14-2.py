# -*- coding: utf-8 -*-
# @Date    : 2021-11-10 10:25:37
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n > 4:
            res *= 3
            res %= int(1e9 + 7)
            n -= 3
        
        return (res * n) % (int(1e9 + 7))