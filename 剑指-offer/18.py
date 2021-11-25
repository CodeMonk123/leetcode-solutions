# -*- coding: utf-8 -*-
# @Date    : 2021-11-19 10:22:22
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        p,q = dummy_head, dummy_head.next
        while q is not None:
            if q.val == val:
                p.next = q.next
                break
            p,q = p.next, q.next
        return dummy_head.next