from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[-1 for _ in range(n)] for _ in range(n)]
        x = 0
        y = 0
        direction = 0
        i = 1
        while i <= n**2:
            if direction == 0:
                while x < n:
                    if ans[y][x] != -1:
                        break
                    ans[y][x] = i
                    i += 1
                    x += 1
                x -= 1
                y += 1
                direction = (direction + 1) % 4
            elif direction == 1:
                while y < n:
                    if ans[y][x] != -1:
                        break
                    ans[y][x] = i
                    i += 1
                    y += 1
                y -= 1
                x -= 1
                direction = (direction + 1) % 4
            elif direction == 2:
                while x >= 0:
                    if ans[y][x] != -1:
                        break
                    ans[y][x] = i
                    i += 1
                    x -= 1
                x += 1
                y -= 1
                direction = (direction + 1) % 4
            else:
                while y >= 0:
                    if ans[y][x] != -1:
                        break
                    ans[y][x] = i
                    i += 1
                    y -= 1
                y += 1
                x += 1
                direction = (direction + 1) % 4
        return ans


solution = Solution()
print(solution.generateMatrix(3))
print(solution.generateMatrix(1))