from typing import List, Tuple
import copy
from collections import OrderedDict


class Solution:
    def __init__(self) -> None:
        self.ans = set()

    def _search(self, num_freq: List[Tuple[int, int]], start: int,
                last_num: int, current: List[int]):
        if start == len(num_freq):
            if len(current) >= 2:
                self.ans.add(tuple(current))
            return

        num, freq = num_freq[start]
        if num < last_num:
            self._search(num_freq, start + 1, last_num, current)
            return
        for i in range(1, freq + 1):
            current_copy = copy.copy(current)
            current_copy += [num] * i
            self._search(num_freq, start + 1, num, current_copy)

        self._search(num_freq, start + 1, last_num, current)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        num_freq = []

        current_num = nums[0]
        count = 0
        for num in nums:
            if num == current_num:
                count += 1
            else:
                num_freq.append((current_num, count))
                count = 1
                current_num = num
        num_freq.append((current_num, count))

        self._search(num_freq, 0, -1e5, [])

        return list(map(lambda x: list(x), self.ans))


solution = Solution()
print(solution.findSubsequences([4, 6, 7, 7]))
print(solution.findSubsequences([4, 4, 3, 2, 1]))
print(solution.findSubsequences([1, 2, 3, 4, 1, 1, 1, 1]))
