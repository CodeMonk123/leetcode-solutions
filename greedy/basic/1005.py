from typing import List
import heapq


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            top = heapq.heappop(nums)
            heapq.heappush(nums, -top)
        return sum(nums)
    
solution = Solution()
print(solution.largestSumAfterKNegations([4,2,3], 1))
print(solution.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))