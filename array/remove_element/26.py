from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


solution = Solution()
print(solution.removeDuplicates([1, 1, 1, 2, 2, 3, 3]))
print(solution.removeDuplicates([]))
print(solution.removeDuplicates([1, 1, 1]))