# -*- coding: utf-8 -*-
# @Date    : 2021-11-19 10:29:19
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def _partition(self, arr:List[int], start:int, end:int)->int:
        split_point = start
        pivot = arr[start]
        for i in range(start+1, end+1):
            if arr[i] <= pivot:
                split_point += 1
                if split_point != i:
                    arr[split_point], arr[i] = arr[i], arr[split_point]
        
        arr[split_point], arr[start] = pivot, arr[split_point]
        return split_point

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr_copy = copy.copy(arr)
        if k == 0:
            return []
        elif k == len(arr_copy):
            return arr_copy
        
        target = k - 1
        start = 0
        end = len(arr_copy) - 1
        while True:
            split_point = self._partition(arr_copy, start, end)
            if split_point == target:
                break
            elif split_point > target:
                end = split_point - 1
            else:
                start = split_point + 1
        
        return arr_copy[:k]
        

solution = Solution()
print(solution.getLeastNumbers([0,1,2,1], 3))
print(solution.getLeastNumbers([0,1,2], 2))
print(solution.getLeastNumbers([4,5,1,6,7,8,2,3], 4))
