class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, int((num + 1) / 2)
        while left <= right:
            mid = int((left + right) / 2)
            res = mid**2
            if res == num:
                return True
            elif res < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


solution = Solution()
print(solution.isPerfectSquare(4))
print(solution.isPerfectSquare(6))