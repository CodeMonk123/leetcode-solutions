# -*- coding: utf-8 -*-
# @Date    : 2021-11-15 16:59:09
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class CQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.length = 0

    def appendTail(self, value: int) -> None:
        self.s1.append(value)
        self.length += 1

    def deleteHead(self) -> int:
        if self.length == 0:
            return -1
        
        if len(self.s2) > 0:
            self.length -= 1
            return self.s2.pop()

        for _ in range(self.length):
            self.s2.append(self.s1.pop())
        
        res = self.s2.pop()
        self.length -= 1
        return res

