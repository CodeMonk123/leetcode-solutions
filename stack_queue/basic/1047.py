class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for ch in s:
            if len(ans) > 0:
                if ans[-1] == ch:
                    ans.pop()
                    continue
            ans.append(ch)

        return ''.join(ans)