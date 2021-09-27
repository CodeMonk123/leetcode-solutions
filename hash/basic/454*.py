from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int],
                     nums3: List[int], nums4: List[int]) -> int:

        sum_ab = {}
        for a in nums1:
            for b in nums2:
                temp = a + b
                if temp not in sum_ab:
                    sum_ab[temp] = 1
                else:
                    sum_ab[temp] += 1

        count = 0
        for c in nums3:
            for d in nums4:
                temp = -(c + d)
                if temp in sum_ab:
                    count += sum_ab[temp]

        return count