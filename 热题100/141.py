# -*- coding: utf-8 -*-
# @Date    : 2021-12-08 10:56:00
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p, q = head, head
        while p is not None and q is not None:
            p = p.next
            if q.next is None:
                return False
            q = q.next.next
            if p == q:
                return True
        return False