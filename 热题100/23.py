# -*- coding: utf-8 -*-
# @Date    : 2021-11-29 10:47:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy_head = ListNode(-1)
        h:List[Tuple[int, ListNode]] = []
        for head in lists:
            if head is not None:
                h.append((head.val, head))

        return dummy_head.next