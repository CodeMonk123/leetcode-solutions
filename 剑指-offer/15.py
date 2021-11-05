# -*- coding: utf-8 -*-
# @Date    : 2021-11-05 10:39:45
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>=1
        return count