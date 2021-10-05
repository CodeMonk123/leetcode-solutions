from typing import List
import copy


class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.k = 0

    def _search(self, need: int, start: int, current: List[int]):
        if len(current) == self.k:
            if need == 0:
                self.ans.append(current)
            return

        if start > need:
            return

        for x in range(start, min(10, need + 1)):
            current_copy = copy.copy(current)
            current_copy.append(x)
            self._search(need - x, start=x + 1, current=current_copy)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.k = k
        self._search(n, 1, [])
        return self.ans


solution = Solution()
print(solution.combinationSum3(3, 7))
print(solution.combinationSum3(3, 9))
print(solution.combinationSum3(9, 45))