# -*- coding: utf-8 -*-
# @Date    : 2021-12-10 11:24:18
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len1, len2 = 0, 0
        p = headA
        while p is not None:
            p = p.next
            len1 += 1
        
        q = headB
        while q is not None:
            q = q.next
            len2 += 1
        
        p, q = headA, headB
        if len1 > len2:
            p, q = q, p
        for _ in range(abs(len1-len2)):
            q = q.next
        
        while p is not None and q is not None:
            if p == q:
                return p
            p = p.next
            q = q.next
        
        return None