from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid = int((start + end) / 2)
            if nums[mid] < target:
                if start == mid:
                    return -1
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                return mid
        return -1


solution = Solution()
print(solution.search([0, 1, 2, 3, 4, 5], 3))
