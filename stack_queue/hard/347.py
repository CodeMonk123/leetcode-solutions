from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        ans = []
        for num, freq in count.items():
            if len(ans) < k:
                heapq.heappush(ans, (freq, num))
            else:
                if ans[0][0] < freq:
                    heapq.heappop(ans)
                    heapq.heappush(ans, (freq, num))

        return [x for _, x in ans]


solution = Solution()
print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
