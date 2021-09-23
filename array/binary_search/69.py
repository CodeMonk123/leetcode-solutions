class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, int((x + 1) / 2)
        while left <= right:
            mid = int((left + right) / 2)
            res1 = mid**2
            res2 = (mid + 1)**2
            if res1 == x or res1 < x and res2 > x:
                return mid
            elif res2 == x:
                return mid + 1
            elif res2 < x:
                left = mid + 1
            elif res1 > x:
                right = mid - 1
        return


solution = Solution()
print(solution.mySqrt(0))
print(solution.mySqrt(4))
print(solution.mySqrt(10))
print(solution.mySqrt(120))