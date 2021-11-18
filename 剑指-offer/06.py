# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 11:22:44
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        reversed_list = self.reversePrint(head.next)
        reversed_list.append(head.val)
        return reversed_list