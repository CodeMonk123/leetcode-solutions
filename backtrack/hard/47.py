from typing import List, Dict
import copy


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def _search(self, count: Dict[int, int], current: List[int]):
        if len(count) == 0:
            self.ans.append(current)
            return

        for num in count:
            count_copy = copy.copy(count)
            current_copy = copy.copy(current)
            count_copy[num] -= 1
            if count_copy[num] == 0:
                count_copy.pop(num)
            current_copy.append(num)
            self._search(count_copy, current_copy)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        self._search(count, [])

        return self.ans


solution = Solution()
print(solution.permuteUnique([1, 1, 2]))
print(solution.permuteUnique([1, 2, 3]))