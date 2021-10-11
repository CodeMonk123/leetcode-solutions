from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        partial_sum = max_sum
        for i in range(1, len(nums)):
            partial_sum = max(0, partial_sum)
            partial_sum += nums[i]
            max_sum = max(max_sum, partial_sum)
    
        return max_sum

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray([-2,1]))