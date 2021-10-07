from typing import List, Tuple
import copy


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def _search(self, num_freq: List[Tuple[int, int]], start: int,
                current: List[int]):
        if start == len(num_freq):
            self.ans.append(current)
            return

        candidate, freq = num_freq[start]
        for i in range(freq + 1):
            current_copy = copy.copy(current)
            current_copy += [candidate] * i
            self._search(num_freq, start + 1, current_copy)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        num_freq = {}
        for num in nums:
            if num not in num_freq:
                num_freq[num] = 1
            else:
                num_freq[num] += 1

        num_freq = list(map(lambda x: (x[0], x[1]), num_freq.items()))
        # print(num_freq)
        self._search(num_freq, 0, [])
        return self.ans


solution = Solution()
print(solution.subsetsWithDup([1, 2, 2]))
print(solution.subsetsWithDup([1, 2, 2, 2]))