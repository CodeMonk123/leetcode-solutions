# -*- coding: utf-8 -*-
# @Date    : 2021-11-19 10:42:05
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min_s = []


    def push(self, x: int) -> None:
        if len(self.s) == 0:
            self.s.append(x)
            self.min_s.append(x)
        else:
            self.s.append(x)
            if x > self.min_s[-1]:
                self.min_s.append(self.min_s[-1])
            else:
                self.min_s.append(x)

    def pop(self) -> None:
        if len(self.s) == 0:
            return None
        self.s.pop()
        self.min_s.pop()


    def top(self) -> int:
        if len(self.s) == 0:
            return -1
        return self.s[-1]


    def min(self) -> int:
        if len(self.min_s) == 0:
            return -1
        return self.min_s[-1]