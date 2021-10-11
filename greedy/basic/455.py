from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sorted_g = sorted(g, reverse=True)
        sorted_s = sorted(s, reverse=True)
        current = 0
        count = 0

        for children in sorted_g:
            if current == len(sorted_s):
                return count
            if sorted_s[current] >= children:
                count += 1
                current += 1
                continue

        
        
        return count
    
solution = Solution()
print(solution.findContentChildren([1,2], [1,2,3]))
print(solution.findContentChildren([1,1], [1,2,3]))
print(solution.findContentChildren([10,9,8,7], [5,6,7,8]))
print(solution.findContentChildren([10,9,8,7], [10,9,8,7]))