from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ''' 有序的正数排序后保持升序，负数排序后保持降序
        只需要找到正负数的分界线，然后归并排序即可
        '''
        if nums[0] >= 0:
            return list(map(lambda x: x**2, nums))
        elif nums[-1] <= 0:
            ans = list(map(lambda x: x**2, nums))
            ans.reverse()
            return ans

        split_point = 0
        for i, value in enumerate(nums):
            if value >= 0:
                split_point = i
                break

        i, j = 0, split_point - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        nums = list(map(lambda x: x**2, nums))
        ans = []
        i, j = 0, split_point
        while i < split_point and j < len(nums):
            if nums[i] < nums[j]:
                ans.append(nums[i])
                i += 1
            else:
                ans.append(nums[j])
                j += 1
        if i < split_point:
            ans += nums[i:split_point]
        else:
            ans += nums[j:]

        return ans


solution = Solution()
print(solution.sortedSquares([-4, -1, 0, 3, 10]))
print(solution.sortedSquares([-10000, -9999, -7, -5, 0, 0, 10000]))
