from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0 for _ in prices] 

        for i in range(1, len(prices)):
            profits[i] = prices[i] - prices[i-1]
        
        return sum(filter(lambda x: x>0, profits))

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([1,2,3,4,5,6]))
print(solution.maxProfit([6,5,4,3,2,1]))