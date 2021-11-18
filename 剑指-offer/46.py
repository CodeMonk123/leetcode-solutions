# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 10:43:18
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:

    def _search(self, rest:str)->int:
        if rest == '':
            return 1
        count = 0
        for i in range(26):
            if rest.startswith(str(i)):
                count += self._search(rest[1 if i/10 < 1 else 2:])
        return count

    def translateNum(self, num: int) -> int:
        return self._search(str(num))

solution = Solution()
print(solution.translateNum(12258))