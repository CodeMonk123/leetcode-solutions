from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


solution = Solution()
print(solution.removeElement([3, 2, 2, 3], 2))
