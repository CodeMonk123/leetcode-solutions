class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for ch in magazine:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        for ch in ransomNote:
            if ch in count:
                if count[ch] < 1:
                    return False
                count[ch] -= 1
            else:
                return False

        return True