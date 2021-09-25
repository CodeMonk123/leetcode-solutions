from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        if height < 1:
            return []
        width = len(matrix[0])
        i, j = 0, 0
        ans = []
        direction = 0
        total = height * width
        while len(ans) < total:
            if direction == 0:
                for _ in range(width):
                    ans.append(matrix[i][j])
                    j += 1
                j -= 1
                i += 1
                direction = (direction + 1) % 4
                height -= 1
            elif direction == 1:
                for _ in range(height):
                    ans.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                width -= 1
                direction = (direction + 1) % 4
            elif direction == 2:
                for _ in range(width):
                    ans.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1
                direction = (direction + 1) % 4
                height -= 1
            else:
                for _ in range(height):
                    ans.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                width -= 1
                direction = (direction + 1) % 4

        return ans


solution = Solution()
print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
