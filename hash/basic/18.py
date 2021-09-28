from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans_set = set()
        for i in range(1, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                start, end = 0, len(nums) - 1
                sub_target = target - nums[i] - nums[j]
                while start < i and end > j:
                    temp = nums[start] + nums[end]
                    if temp > sub_target:
                        end -= 1
                    elif temp < sub_target:
                        start += 1
                    else:
                        ans_set.add((nums[start], nums[i], nums[j], nums[end]))
                        start += 1
                        end -= 1

        return list(map(lambda x: list(x), ans_set))


solution = Solution()
print(solution.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
