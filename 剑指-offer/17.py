# -*- coding: utf-8 -*-
# @Date    : 2021-11-17 11:21:03
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def printNumbers(self, n:int)->List[int]:
        return [x for x in range(1, int(10**n))]