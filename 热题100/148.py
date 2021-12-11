# -*- coding: utf-8 -*-
# @Date    : 2021-12-09 10:59:52
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple, Optional
import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, head1:ListNode, head2:ListNode)->ListNode:
        p, q = head1, head2
        dummy_head = ListNode()
        r = dummy_head
        while p is not None and q is not None:
            if p.val < q.val:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next
            r = r.next
        
        if p is not None:
            r.next = p
        else:
            r.next = q

        return dummy_head.next
    
    def merge_sort(self, head:ListNode)->ListNode:
        p,q = head, head
        while q is not None:
            if q.next is None:
                break
            q = q.next
            if q.next is None:
                break
            q=q.next
            p=p.next
        if p == q:
            return head
        head1 = head
        head2 = p.next
        p.next = None

        head1 = self.merge_sort(head1)
        head2 = self.merge_sort(head2)
        return self.merge(head1, head2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        return self.merge_sort(head)