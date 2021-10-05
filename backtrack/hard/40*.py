from typing import List, Tuple
import copy


class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.target = 0

    def _search(self, candidate_freq: List[Tuple[int, int]], start: int,
                need: int, current: List[int]):
        if need < 0:
            return
        if need == 0:
            self.ans.append(current)
            return

        for i in range(start, len(candidate_freq)):
            candidate, freq = candidate_freq[i]
            if candidate > need:
                return
            for j in range(freq):
                current_copy = copy.copy(current)
                current_copy += [candidate] * (j + 1)
                self._search(candidate_freq, i + 1, need - candidate * (j + 1),
                             current_copy)

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        self.target = target
        self.ans = []

        count = {}
        for candidate in candidates:
            if candidate not in count:
                count[candidate] = 1
            else:
                count[candidate] += 1

        candidate_freq = []
        for k in sorted(count.keys()):
            candidate_freq.append((k, count[k]))

        self._search(candidate_freq, 0, target, [])
        return self.ans


solution = Solution()
print(solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
print(solution.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
print(
    solution.combinationSum2([
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1
    ], 27))
