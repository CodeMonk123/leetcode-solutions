class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        p, q, r = 1, 2, 0
        for _ in range(n-2):
            r = p + q
            p, q = q, r
        
        return r