from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        partial_sum = 0
        min_length = len(nums) + 1

        for right, val in enumerate(nums):
            partial_sum += val
            while partial_sum >= target:
                min_length = min(min_length, right - left + 1)
                partial_sum -= nums[left]
                left += 1

        return min_length if min_length <= len(nums) else 0


solution = Solution()
print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(solution.minSubArrayLen(4, [1, 4, 4]))
print(solution.minSubArrayLen(11, [1, 2, 3, 4, 5]))