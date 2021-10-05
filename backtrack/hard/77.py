from typing import List
from copy import copy


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def search(self, current: int, need: int, n: int, combination: List[int]):
        if need == 0:
            self.ans.append(combination)
            return
        if n - current < need:
            return

        combination_copy = copy(combination)
        combination.append(current + 1)
        self.search(current + 1, need - 1, n, combination)
        self.search(current + 1, need, n, combination_copy)

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.search(0, k, n, [])
        return self.ans
