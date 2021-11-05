# -*- coding: utf-8 -*-
# @Date    : 2021-11-02 10:53:38
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy
from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> str:
        count = OrderedDict()
        for ch in s:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
        
        for k,v in count.items():
            if v == 1:
                return k
        
        return ' '