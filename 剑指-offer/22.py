# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 15:51:00
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        length = 0
        p = head
        while p is not None:
            length += 1
            p = p.next
        
        if k > length:
            return None

        p = head
        for i in range(length - k):
            p = p.next
        
        return p