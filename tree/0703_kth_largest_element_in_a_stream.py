from typing import List
from heapq import heapify, heappush, heappop


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = list()
        for x in nums:
            heappush(self.heap, x)
            if len(self.heap) > k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) != self.k:
            heappop(self.heap)
        return self.heap[0]


class KthLargest1:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapify(self.nums)

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        while len(self.nums) != self.k:
            heappop(self.nums)
        return self.nums[0]


def test_kth_largest():
    obj = KthLargest(3, [4, 5, 8, 2])
    assert obj.add(3) == 4, 'wrong result'
    assert obj.add(5) == 5, 'wrong result'
    assert obj.add(10) == 5, 'wrong result'
    assert obj.add(9) == 8, 'wrong result'
    assert obj.add(4) == 8, 'wrong result'


if __name__ == '__main__':
    test_kth_largest()
