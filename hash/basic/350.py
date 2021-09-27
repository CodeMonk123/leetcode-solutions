from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        for num in nums1:
            if num in count1:
                count1[num] += 1
            else:
                count1[num] = 1

        count2 = {}
        for num in nums2:
            if num in count1:
                if num not in count2:
                    count2[num] = 1
                else:
                    count2[num] = min(count1[num], count2[num] + 1)

        ans = []
        for num in count2:
            ans += [num] * count2[num]

        return ans