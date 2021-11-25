# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 15:39:02
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    class Node:
        def __init__(self, val) -> None:
            self.val = val
            self.next = None

    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        head: Solution.Node = Solution.Node(-1)
        tail: Solution.Node = None


        for num in nums:
            if num % 2 == 1:
                p = Solution.Node(num)
                p.next = head.next
                head.next = p
                if tail is None:
                    tail = p
            else:
                p = Solution.Node(num)
                if tail is None:
                    tail = head
                tail.next = p
                tail = p
        
        res = []
        p = head.next
        while p is not None:
            res.append(p.val)
            p = p.next
        
        return res

solution = Solution()
print(solution.exchange([1,2,3,4]))
print(solution.exchange([21,235,46,745,7,23,4,3,43,5,23,52,5,]))