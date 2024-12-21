from heapq import heappop, heappush


class Allocator:
    def __init__(self, n: int):
        self.nums = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i, x in enumerate(self.nums):
            if x:
                cnt = 0
            else:
                cnt += 1
                if cnt == size:
                    self.nums[i - size + 1: i + 1] = [mID] * size
                    return i - size + 1
        return  -1

    def freeMemory(self, mID: int) -> int:
        cnt = 0
        for i, x in enumerate(self.nums):
            if x == mID:
                cnt += 1
                self.nums[i] = 0
        return cnt


def test_allocator():
    obj = Allocator(10)
    assert obj.allocate(1 ,1) == 0, 'wrong result'
    assert obj.allocate(1 ,2) == 1, 'wrong result'
    assert obj.allocate(1 ,3) == 2, 'wrong result'
    assert obj.freeMemory(2) == 1, 'wrong result'
    assert obj.allocate(3 ,4) == 3, 'wrong result'
    assert obj.allocate(1 ,1) == 1, 'wrong result'
    assert obj.allocate(1 ,1) == 6, 'wrong result'
    assert obj.freeMemory(1) == 3, 'wrong result'
    assert obj.allocate(10, 2) == -1, 'wrong result'
    assert obj.freeMemory(7) == 0, 'wrong result'


if __name__ == '__main__':
    test_allocator()
