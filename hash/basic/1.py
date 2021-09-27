from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = sorted(zip(nums, list(range(len(nums)))),
                           key=lambda x: x[0])

        start, end = 0, len(num_index) - 1
        while start < end:
            if num_index[start][0] + num_index[end][0] == target:
                return [num_index[start][1], num_index[end][1]]
            elif num_index[start][0] + num_index[end][0] < target:
                start += 1
            else:
                end -= 1
        return [-1, -1]


solution = Solution()
print(solution.twoSum([2, 7, 123, 415, 52, 5], 9))
