# -*- coding: utf-8 -*-
# @Date    : 2021-12-08 11:31:01
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast is not None:
            slow = slow.next
            if fast.next is None:
                return None
            fast = fast.next.next
            if slow == fast:
                break
        
        if fast is None:
            return None
        
        p = head
        while p != slow:
            p = p.next
            slow = slow.next
        
        return p