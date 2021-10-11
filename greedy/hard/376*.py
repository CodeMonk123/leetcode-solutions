from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        count = 1

        pre_diff = 0

        for i in range(0, len(nums) - 1):
            cur_diff = nums[i + 1] - nums[i]
            if cur_diff > 0 and pre_diff <= 0 or pre_diff >=0 and cur_diff < 0:
                count += 1
                pre_diff = cur_diff
            
        

        return count


solution = Solution()
print(solution.wiggleMaxLength([1,7,4,9,2,5]))
print(solution.wiggleMaxLength([1,1,1,1,1]))
print(solution.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(solution.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
print(solution.wiggleMaxLength([486,431,132,46,441,383,199,476,87,225,491,3,315,32,441,195,188,72,299,404,224,473,124,279,301,145,429,77,423,472,388,387,29,348,22,327,276,448,396,269,382,436,382,160,156,34,303,264,271,409]))    
        