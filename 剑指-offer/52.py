# -*- coding: utf-8 -*-
# @Date    : 2021-11-17 10:59:27
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
        length1 = 0
        length2 = 0
        p = headA
        while p is not None:
            p = p.next
            length1 += 1
        
        q = headB
        while q is not None:
            q = q.next
            length2 += 1
        
        p,q = headA, headB
        if length1 > length2:
            for i in range(length1 - length2):
                p = p.next
        elif length2 > length1:
            for i in range(length2 - length1):
                q = q.next
        
        while p != q:
            p, q = p.next, q.next
        
        return p