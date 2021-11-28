from typing import List
from collections import Counter


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.freq2[self.nums2[index]] -= 1

        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for k, v in self.freq1.items():
            res += v * self.freq2[tot - k]
        return res


def test_find_sum_pairs():
    findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
    assert findSumPairs.count(7) == 8, 'wrong result'
    findSumPairs.add(3, 2)
    assert findSumPairs.count(8) == 2, 'wrong result'
    assert findSumPairs.count(4) == 1, 'wrong result'
    findSumPairs.add(0, 1)
    findSumPairs.add(1, 1)
    assert findSumPairs.count(7) == 11, 'wrong result'


if __name__ == '__main__':
    test_find_sum_pairs()

