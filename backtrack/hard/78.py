from typing import List
import copy


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def _search(self, nums: List[int], start: int, current: List[int]):
        if start == len(nums):
            self.ans.append(current)
            return

        copy_current = copy.copy(current)
        copy_current.append(nums[start])
        self._search(nums, start + 1, copy_current)
        self._search(nums, start + 1, current)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self._search(nums, 0, [])
        return self.ans


solution = Solution()
print(solution.subsets([1, 2, 3, 4]))
