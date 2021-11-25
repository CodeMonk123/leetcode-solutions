# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 15:00:18
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 1:
            return True
        root_val = postorder[-1]
        left_end = 0
        for i in range(len(postorder) - 1):
            if postorder[i] < root_val:
                left_end = i
            else:
                break
        right_start = left_end + 1
        for i in range(right_start, len(postorder)-1):
            if postorder[i] < root_val:
                return False
        
        return self.verifyPostorder(postorder[0:left_end+1]) and self.verifyPostorder(postorder[right_start:-1])


solution = Solution()
print(solution.verifyPostorder([1,6,3,2,5]))
print(solution.verifyPostorder([1,3,2,6,5]))