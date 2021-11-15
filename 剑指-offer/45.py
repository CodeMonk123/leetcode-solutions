# -*- coding: utf-8 -*-
# @Date    : 2021-11-11 16:25:38
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def lt(self, a:int, b:int)->bool:
        if a == 0:
            return True
        elif b == 0:
            return False
        
        digit_a = []
        digit_b = []
        while a != 0:
            digit_a.append(a % 10)
            a //= 10
        
        while b != 0:
            digit_b.append(b % 10)
            b //= 10
        
        digit_a.reverse()
        digit_b.reverse()

        return tuple(digit_a + digit_b) < tuple(digit_b + digit_a)
    
    def partition(self, nums:List[int], start:int, end:int)->int:
        pivot = nums[start]
        split_point = start
        for i in range(start+1, end+1):
            if self.lt(nums[i], pivot):
                split_point += 1
                if split_point != i:
                    nums[split_point], nums[i] = nums[i], nums[split_point]
        nums[start], nums[split_point] = nums[split_point], pivot
        return split_point

    def qsort(self, nums:List[int], start:int, end:int):
        if start < end:
            split_point = self.partition(nums, start, end)
            self.qsort(nums, start, split_point-1)
            self.qsort(nums, split_point + 1, end)
        
    def minNumber(self, nums: List[int]) -> str:
        self.qsort(nums, 0, len(nums) - 1)
        print(nums)
        return ''.join(map(str, nums))
    
solution = Solution()
print(solution.minNumber([3, 30, 34, 5, 9]))
print(solution.minNumber([10, 3]))
print(solution.minNumber([128, 12]))
print(solution.lt(30, 3))
print(solution.minNumber([824,938,1399,5607,6973,5703,9609,4398,8247]))
print(solution.minNumber([121, 12]))