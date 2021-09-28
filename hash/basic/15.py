from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        num_idx = sorted(zip(nums, list(range(len(nums)))))
        for i, (num, idx) in enumerate(num_idx):
            target = -num
            start, end = i + 1, len(num_idx) - 1
            while start < end:
                temp = num_idx[start][0] + num_idx[end][0]
                if temp > target:
                    end -= 1
                elif temp < target:
                    start += 1
                else:
                    ans.add(
                        tuple(sorted([num, num_idx[start][0],
                                      num_idx[end][0]])))
                    start += 1
                    end -= 1

        return list(map(lambda x: list(x), ans))


solution = Solution()
print(solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
