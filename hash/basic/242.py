class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        print(count)
        for c in t:
            if c in count:
                count[c] -= 1
            else:
                count[c] = -1

        print(count)

        for val in count.values():
            if val != 0:
                return False

        return True


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
