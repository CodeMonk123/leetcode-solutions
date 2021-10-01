from typing import List, Tuple


class MyMaxHeap(object):
    def __init__(self) -> None:
        super().__init__()
        self.nums: List[Tuple[int, int]] = []
        self.index_map = {}

    def add(self, num, index):
        self.nums.append((num, index))
        self._sift_up(len(self.nums) - 1)

    def top(self) -> Tuple[int, int]:
        if len(self.nums) == 0:
            return None
        else:
            return self.nums[0]

    def pop(self) -> Tuple[int, int]:
        # print("pop", self.nums)
        if len(self.nums) == 0:
            return None
        else:
            res = self.nums[0]
            self.nums[0] = self.nums[-1]
            self.nums.pop(-1)
            if len(self.nums) > 0:
                self._sift_down(0)
            return res

    def _sift_down(self, start: int) -> None:
        i, j = start, 2 * start + 1
        temp = self.nums[i]
        while j < len(self.nums):
            if j < len(self.nums) - 1 and self.nums[j][0] < self.nums[j +
                                                                      1][0]:
                j += 1
            if self.nums[j][0] < temp[0]:
                break
            else:
                self.nums[i] = self.nums[j]
                i = j
                j = 2 * i + 1
        self.nums[i] = temp

    def _sift_up(self, start: int) -> None:
        i, j = start, int((start - 1) / 2)
        temp = self.nums[i]
        while i > 0:
            if temp[0] < self.nums[j][0]:
                break
            else:
                self.nums[i] = self.nums[j]
                i = j
                j = int((i - 1) / 2)
        self.nums[i] = temp


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = MyMaxHeap()
        for i in range(len(nums)):
            heap.add(nums[i], i)
            if i >= k - 1:
                while True:
                    max_val, index = heap.top()
                    if index < i + 1 - k:
                        # print('i={}, k={}, index={}'.format(i, k, index))
                        heap.pop()
                    else:
                        ans.append(max_val)
                        break

        return ans


solution = Solution()
print(solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(solution.maxSlidingWindow(nums=[1, -1], k=1))
print(solution.maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3))
print(solution.maxSlidingWindow(nums=[1, -9, 8, -6, 6, 4, 0, 5], k=4))
