# -*- coding: utf-8 -*-
# @Date    : 2021-11-29 10:36:05
# @Author  : CodeMonk123

from typing import List, Optional
from typing import Dict, Tuple,Optional
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        p = dummy_head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                p.next = list1
                p = list1
                list1 = list1.next
            else:
                p.next = list2
                p = list2
                list2 = list2.next
        
        if list1 is not None:
            p.next = list1
        else:
            p.next = list2


        return dummy_head.next