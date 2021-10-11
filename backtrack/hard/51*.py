from typing import List, Tuple


class Solution:
    def __init__(self) -> None:
        self._placements: List[List[str]] = []

    def _placement_format(self, placement: List[Tuple[int, int]]) -> List[str]:
        ans = []
        n = len(placement)
        for coordinate in placement:
            line = ['.' for _ in range(n)]
            line[coordinate[1]] = 'Q'
            line = ''.join(line)
            ans.append(line)
        return ans

    def _place_next_queue(self, n: int, current_placement: List[Tuple[int,
                                                                      int]]):
        if len(current_placement) == n:
            self._placements.append(self._placement_format(current_placement))
            return
        else:
            x = len(current_placement)
            for y in range(n):
                new_coordinate = (x, y)
                is_available = True
                for coordinate in current_placement:
                    if coordinate[1] == new_coordinate[1] or abs(
                            coordinate[0] -
                            new_coordinate[0]) == abs(coordinate[1] -
                                                      new_coordinate[1]):
                        is_available = False
                        break
                if is_available:
                    current_placement.append(new_coordinate)
                    self._place_next_queue(n, current_placement)
                    current_placement.pop()

    def solveNQueens(self, n: int) -> List[List[str]]:
        self._placements = []
        self._place_next_queue(n, [])
        return self._placements


solution = Solution()
print(solution.solveNQueens(4))
print(solution.solveNQueens(3))
print(solution.solveNQueens(1))