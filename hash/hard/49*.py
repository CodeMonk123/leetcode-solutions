from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in ans_dict:
                ans_dict[sorted_str] = [str]
            else:
                ans_dict[sorted_str].append(str)

        return list(ans_dict.values())


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
