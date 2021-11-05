# -*- coding: utf-8 -*-
# @Date    : 2021-11-04 14:39:08
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) < 2:
            return True
        
        stack = []

        i,j = 0, 0

        for i in range(len(popped)):
            while len(stack) == 0 or  stack[-1] != popped[i] and j < len(pushed):
                stack.append(pushed[j])
                j+=1
            if stack[-1] == popped[i]:
                stack.pop()
                i+=1
        
        return len(stack) == 0
            


solution = Solution()

print(solution.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(solution.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))