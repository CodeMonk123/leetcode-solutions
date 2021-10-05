from typing import List
import copy


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def _search(self, s: str, current: List[str]):
        if s == "":
            self.ans.append(current)
            return

        current_copy = copy.copy(current)
        current_copy.append(s[0])
        self._search(s[1:], current_copy)

        for i in range(1, len(s)):
            start, end = 0, i
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    break
            if start >= end:
                current_copy = copy.copy(current)
                current_copy.append(s[:i + 1])
                self._search(s[i + 1:], current_copy)

    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self._search(s, [])
        return self.ans


solution = Solution()
print(solution.partition('aab'))
print(solution.partition('a'))
print(solution.partition('bb'))
print(solution.partition('efe'))