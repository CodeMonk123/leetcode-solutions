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
        tail = dummy_head
        h:List[Tuple[int, ListNode]] = []
        for head in lists:
            if head is not None:
                h.append((head.val, id(head), head))
        
        heapq.heapify(h)
        while len(h) > 0:
            _, _, next_node = heapq.heappop(h)
            tail.next = next_node
            tail = next_node
            if next_node.next is not None:
                heapq.heappush(h, (next_node.next.val, id(next_node.next), next_node.next))


        return dummy_head.next