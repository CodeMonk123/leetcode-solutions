# -*- coding: utf-8 -*-
# @Date    : 2021-11-19 10:26:38
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        q = head
        while q is not None:
            next_q = q.next
            q.next = p
            p = q
            q = next_q
        return p