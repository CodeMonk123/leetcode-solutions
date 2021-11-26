# -*- coding: utf-8 -*-
# @Date    : 2021-11-26 16:30:36
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(val=-1)
        p = dummy_head
        overflow = 0
        while l1 is not None and l2 is not None:
            temp = l1.val + l2.val + overflow
            overflow = temp // 10
            temp %= 10
            new_node = ListNode(val=temp)
            p.next = new_node
            p = p.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 is None:
            while l2 is not None:
                temp = l2.val + overflow
                overflow = temp // 10
                temp %= 10
                new_node = ListNode(val=temp)
                p.next = new_node
                p = p.next
                l2 = l2.next
            if overflow != 0:
                new_node = ListNode(val=overflow)
                p.next = new_node
        elif l2 is None:
            while l1 is not None:
                temp = l1.val + overflow
                overflow = temp // 10
                temp %= 10
                new_node = ListNode(val=temp)
                p.next = new_node
                p = p.next
                l1 = l1.next
            if overflow != 0:
                new_node = ListNode(val=overflow)
                p.next = new_node

        return dummy_head.next