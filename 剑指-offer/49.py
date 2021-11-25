# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 15:15:03
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def first_ugly_number_ge_x(self, x:int, ugly_nums:List[int])->int:
        start, end = 0, len(ugly_nums) - 1
        while start < end:
            mid = (start + end) // 2
            if ugly_nums[mid] == x:
                return ugly_nums[mid]
            elif ugly_nums[mid] < x:
                start = mid + 1
            else:
                end = mid
        return ugly_nums[start]

        


    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1,2,3,4,5]
        if n <= 5:
            return ugly_nums[n-1]
        
        for i in range(5, n):
            current_max = ugly_nums[-1]
            x1 = self.first_ugly_number_ge_x(current_max // 2 + 1, ugly_nums)
            x2 = self.first_ugly_number_ge_x(current_max // 3 + 1, ugly_nums)
            x3 = self.first_ugly_number_ge_x(current_max // 5 + 1, ugly_nums)
            ugly_nums.append(min(x1 * 2, x2 * 3, x3 * 5))
        
        return ugly_nums[-1]

solution = Solution()
for i in range(1,150):
    print(solution.nthUglyNumber(i))