from typing import List, Set
import copy


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def _search(self, nums: Set[int], current: List[int]):
        if len(nums) == 0:
            self.ans.append(current)
            return

        for ele in nums:
            nums_copy = copy.copy(nums)
            current_copy = copy.copy(current)
            nums_copy.remove(ele)
            current_copy.append(ele)
            self._search(nums_copy, current_copy)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self._search(set(nums), [])
        return self.ans