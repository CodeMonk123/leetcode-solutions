# -*- coding: utf-8 -*-
# @Date    : 2021-11-28 15:10:58
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(-1, head)
        length = 0
        p = head
        while p is not None:
            length += 1
            p = p.next
        
        q = dummy_head
        p = head
        for _ in range(length - n):
            p = p.next
            q = q.next
        q.next = p.next
        return dummy_head.next