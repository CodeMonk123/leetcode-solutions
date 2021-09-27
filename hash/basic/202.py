from typing import List
from functools import reduce


class Solution:
    def _to_digits(self, n: int) -> List[int]:
        digits = []
        while n != 0:
            digits.append(n % 10)
            n = int(n / 10)

        return digits

    def isHappy(self, n: int) -> bool:
        history = set()
        while True:
            digits = self._to_digits(n)
            print(digits)
            result = sum(map(lambda x: x**2, digits))
            print(result)
            if result == 1:
                return True
            if result in history:
                return False
            history.add(result)
            n = result


solution = Solution()
print(solution.isHappy(7))
