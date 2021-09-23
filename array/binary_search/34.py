from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        # find the first
        first_idx = -1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                first_idx = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # find the last
        last_idx = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                last_idx = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [first_idx, last_idx]


solution = Solution()
print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
