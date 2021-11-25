# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 16:35:57
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        return (self.lastRemaining(n-1, m) + m ) % n