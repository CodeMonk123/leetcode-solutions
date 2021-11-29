# -*- coding: utf-8 -*-
# @Date    : 2021-11-29 10:55:55
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def _reverse(self, nums:List[int], i,j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                k = i
        
        if k == -1:
            nums.reverse()
            return
        
        l = k + 1
        for i in range(k+1, len(nums)):
            if nums[i] > nums[k]:
                l = i

        nums[k], nums[l] = nums[l], nums[k]
        self._reverse(nums, k+1, len(nums)-1)

        