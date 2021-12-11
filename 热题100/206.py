# -*- coding: utf-8 -*-
# @Date    : 2021-12-11 15:21:29
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        p = head
        if p is not None:
            q = p.next
            p.next = None
            while q is not None:
                new_q = q.next
                q.next = p
                p = q
                q = new_q

            return p


        return None