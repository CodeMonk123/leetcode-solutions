# -*- coding: utf-8 -*-
# @Date    : 2021-11-26 16:51:35
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def find_kth_in_two_arrays(self, k:int, nums1:List[int], nums2:List[int]) ->int:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.find_kth_in_two_arrays(k, nums2, nums1)
        
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        
        p1 = min(m, k // 2)
        p2 = k - p1
        if nums1[p1 - 1] < nums2[p2 - 1]:
            return self.find_kth_in_two_arrays(k - p1, nums1[p1:], nums2)
        else:
            return self.find_kth_in_two_arrays(k - p2, nums1, nums2[p2:])


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return self.find_kth_in_two_arrays((m+n)//2 + 1, nums1, nums2)
        else:
            e1 =  self.find_kth_in_two_arrays((m+n)//2, nums1, nums2)
            e2 =  self.find_kth_in_two_arrays((m+n)//2 + 1, nums1, nums2)
            return (e1 + e2) / 2

solution = Solution()
print(solution.findMedianSortedArrays([1,3], [2]))