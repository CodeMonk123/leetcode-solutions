class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dict = {}
        for c in list(t):
            if c in target_dict:
                target_dict[c] += 1
            else:
                target_dict[c] = 1

        min_length = len(s) + 1
        min_left, min_right = 0, 0
        right, left = 0, 0

        def validate(d: dict) -> bool:
            for k in d:
                if d[k] > 0:
                    return False
            return True

        while right < len(s):
            if s[right] in target_dict:
                target_dict[s[right]] -= 1

            while validate(target_dict):
                if right + 1 - left < min_length:
                    min_length = right + 1 - left
                    min_left = left
                    min_right = right
                if s[left] in target_dict:
                    target_dict[s[left]] += 1
                left += 1
            right += 1

        return s[min_left:min_right + 1] if min_length <= len(s) else ''


solution = Solution()
print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
print(solution.minWindow(s="a", t="aa"))