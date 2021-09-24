class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        slow1, fast = 0, 0
        s = list(s.lstrip('#'))
        t = list(t.lstrip('#'))
        while fast < len(s):
            if s[fast] == '#':
                if slow1 > 0:
                    slow1 -= 1
            else:
                s[slow1] = s[fast]
                slow1 += 1
            fast += 1

        slow2, fast = 0, 0
        while fast < len(t):
            if t[fast] == '#':
                if slow2 > 0:
                    slow2 -= 1
            else:
                t[slow2] = t[fast]
                slow2 += 1
            fast += 1

        return s[:slow1] == t[:slow2]


solution = Solution()
print(solution.backspaceCompare('ab#c', 'ad#c'))
print(solution.backspaceCompare('ab##', 'c#d#'))
print(solution.backspaceCompare('a#c', 'b'))