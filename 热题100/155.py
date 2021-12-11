# -*- coding: utf-8 -*-
# @Date    : 2021-12-10 11:22:06
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.min_s) == 0 or self.min_s[-1] > val:
            self.min_s.append(val)
        else:
            self.min_s.append(self.min_s[-1])

    def pop(self) -> None:
        self.s.pop()
        self.min_s.pop()


    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()