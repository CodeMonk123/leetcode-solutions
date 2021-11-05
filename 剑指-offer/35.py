# -*- coding: utf-8 -*-
# @Date    : 2021-11-04 14:12:09
# @Author  : CodeMonk123

from typing import List, Mapping
from typing import Dict, Tuple
import copy

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head:Node)->Node :
        if head is None:
            return None
        
        p = head
        while p is not None:
            q = Node(p.val,p.next, None)
            p.next = q
            p = q.next
        
        p = head
        while p is not None:
            q = p.next
            q.random = p.random.next if p.random is not None else None
            p = q.next
        

        new_head = head.next
        p = head
        q = new_head
        while p is not None:
            p.next = q.next
            q.next = p.next.next if p.next is not None else None
            p = p.next
            q = q.next

        return new_head
    
    def copyRandomList2(self, head:Node)->Node:
        if head is None:
            return None
        
        node_map = {None:None}
        p = head
        while p is not None:
            q = Node(p.val, None, None)
            node_map[p] = q
            p = p.next

        p = head
        while p is not None:
            node_map[p].next = node_map[p.next]
            node_map[p].random = node_map[p.random]
            p = p.next
        
        return node_map[head]