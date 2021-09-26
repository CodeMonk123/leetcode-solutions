from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(s) < len(p):
            return ans
        count = dict()
        for ch in p:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

        start, end = 0, 0
        count2 = {k: v for k, v in count.items()}

        while end < len(s):
            if s[end] not in count2:
                start = end + 1
                end = end + 1
                count2 = {k: v for k, v in count.items()}
            else:
                count2[s[end]] -= 1
                if count2[s[end]] < 0:
                    for i in range(start, end):
                        if s[i] == s[end]:
                            start = i + 1
                            count2[s[end]] = 0
                            break
                        else:
                            count2[s[i]] += 1
                elif count2[s[end]] == 0:
                    if len(set(count2.values())) == 1:
                        ans.append(start)
                        count2[s[start]] = 1
                        start += 1
                end += 1

        return ans


solution = Solution()
print(solution.findAnagrams(s="abcab", p="ab"))
print(solution.findAnagrams(s="abaacbabc", p="abc"))
print(solution.findAnagrams(s="cabab", p="ab"))