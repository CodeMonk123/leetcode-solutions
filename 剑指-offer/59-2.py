# -*- coding: utf-8 -*-
# @Date    : 2021-11-15 11:09:47
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class MaxQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.length = 0


    def max_value(self) -> int:
        if self.length == 0:
            return -1
        
        return self.q2[0]


    def push_back(self, value: int) -> None:
        if self.length == 0:
            self.q2.append(value)
            self.length = 1
        else:
            if value > self.q2[0]:
                self.q1 += self.q2
                self.q2 = [value]
            else:
                self.q2.append(value)
            self.length += 1


    def pop_front(self) -> int:
        if self.length == 0:
            return -1
        elif len(self.q1) == 0:
            res = self.q2[0]
            self.q2.pop(0)
            self.length -= 1
            # Todo
            if len(self.q2) != 0:
                max_value = self.q2[0]
                max_index = 0
                for i in range(1, len(self.q2)):
                    if self.q2[i] > max_value:
                        max_value = self.q2[i]
                        max_index = i
                self.q1 += self.q2[:max_index]
                self.q2 = self.q2[max_index:]

            return res
        else:
            res = self.q1[0]
            self.q1.pop(0)
            self.length -= 1
            return res
