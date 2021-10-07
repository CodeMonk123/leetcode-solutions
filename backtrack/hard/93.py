from typing import List
import copy


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def _search(self, s: str, start: int, need: int, current: List[str]):
        if need == 0:
            if start == len(s):
                self.ans.append('.'.join(current))
            return

        else:
            if start < len(s) and s[start] == '0':
                copy_current = copy.copy(current)
                copy_current.append(s[start])
                self._search(s, start + 1, need - 1, copy_current)
                return
            for i in range(1, 4):
                if start + i > len(s):
                    return
                if i < 3:
                    copy_current = copy.copy(current)
                    copy_current.append(s[start:start + i])
                    self._search(s, start + i, need - 1, copy_current)
                else:
                    if int(s[start:start + 3]) <= 255:
                        copy_current = copy.copy(current)
                        copy_current.append(s[start:start + i])
                        self._search(s, start + i, need - 1, copy_current)

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self._search(s, 0, 4, [])
        return self.ans


solution = Solution()
print(solution.restoreIpAddresses("25525511135"))
print(solution.restoreIpAddresses("0000"))
print(solution.restoreIpAddresses("010010"))