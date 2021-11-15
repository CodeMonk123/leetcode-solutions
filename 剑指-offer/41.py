# -*- coding: utf-8 -*-
# @Date    : 2021-11-11 15:40:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy
import heapq
from queue import PriorityQueue


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []    



    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 and len(self.min_heap) == 0:
            self.max_heap.append(num * -1)
            return
        
        if len(self.max_heap) == 1 and len(self.min_heap) == 0:
            if num > self.max_heap[0] * -1:
                self.min_heap.append(num)
            else:
                self.min_heap.append(self.max_heap[0] * -1)
                self.max_heap[0] = -num
            return

        
        if len(self.max_heap) == len(self.min_heap):
            if num < self.min_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                min_top = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -min_top)
                heapq.heappush(self.min_heap, num)
            return
        else:
            if num > self.max_heap[0] * -1:
                heapq.heappush(self.min_heap, num)
            else:
                max_top = heapq.heappop(self.max_heap) * -1
                heapq.heappush(self.min_heap, max_top)
                heapq.heappush(self.max_heap, num * -1)
        

    def findMedian(self) -> float:
        if len(self.max_heap) == 0 and len(self.min_heap) == 0:
            return 0
        
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] * -1 + self.min_heap[0]) / 2
        else:
            return self.max_heap[0] * -1


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()